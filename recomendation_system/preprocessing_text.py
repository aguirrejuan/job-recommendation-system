import re
import pandas as pd
from unicodedata import normalize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk
nltk.download('stopwords')
nltk.download('punkt')


def preprocess_text(text):
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Normalize text to remove accents and diacritics
    text = normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')

    # Tokenize text into words
    words = word_tokenize(text)

    # Remove stopwords
    stopwords_list = set(stopwords.words('english') +
                         stopwords.words('spanish'))
    words = [word.lower()
             for word in words if word.lower() not in stopwords_list]

    # Perform stemming
    stemmer = SnowballStemmer('english')
    words = [stemmer.stem(word) for word in words]

    # Join words back into a normalized sentence
    normalized_text = ' '.join(words)

    return normalized_text


def job_preprocessing(area, work_modality, country, city, remote,
                      vacancy_name, description):
    job_description = "Job Description:\n"

    if not pd.isna(vacancy_name):
        job_description += f"Vacancy Name: {preprocess_text(vacancy_name)}\n"

    if not pd.isna(area):
        job_description += f"Area: {preprocess_text(area)}\n"

    if not pd.isna(work_modality):
        job_description += f"Work Modality: {preprocess_text(work_modality)}\n"

    if not pd.isna(country) and not pd.isna(city):
        job_description += f"Location: {preprocess_text(country)},\
             {preprocess_text(city)}\n"
             
    elif not pd.isna(country):
        job_description += f"Location: {preprocess_text(country)}\n"
    elif not pd.isna(city):
        job_description += f"Location: {preprocess_text(city)}\n"

    if not pd.isna(remote):
        job_description += f"Remote: {preprocess_text(str(remote))}\n"

    if not pd.isna(description):
        job_description += f"Description:\n{preprocess_text(description)}\n"

    return job_description


def user_preprocessing(country, area, subareas, degrees,
                       wage_aspiration, currency,
                       current_wage, change_cities,
                       language, years_experience,
                       months_experience, wish_role_name,
                       work_modality, hardskills):
    job_profile = "Job Search Profile:\n"

    if not pd.isna(country):
        job_profile += f"Country: {preprocess_text(country)}\n"

    if not pd.isna(area):
        job_profile += f"Area: {preprocess_text(area)}\n"

    if not pd.isna(subareas):
        job_profile += f"Subareas: {preprocess_text(subareas)}\n"

    if not pd.isna(degrees):
        job_profile += f"Degrees: {preprocess_text(degrees)}\n"

    if not pd.isna(wage_aspiration):
        job_profile += f"Wage Aspiration: {wage_aspiration} {currency}\n"

    if not pd.isna(current_wage):
        job_profile += f"Current Wage: {current_wage} {currency}\n"

    if not pd.isna(change_cities):
        job_profile += f"Open to Change Cities:\
             {preprocess_text(str(change_cities))}\n"

    if not pd.isna(language):
        job_profile += f"Language: {preprocess_text(language)}\n"

    if not pd.isna(years_experience):
        job_profile += f"Years of Experience: {years_experience}\n"

    if not pd.isna(months_experience):
        job_profile += f"Months of Experience: {months_experience}\n"

    if not pd.isna(wish_role_name):
        job_profile += f"Wish Role Name: {preprocess_text(wish_role_name)}\n"

    if not pd.isna(work_modality):
        job_profile += f"Work Modality: {preprocess_text(work_modality)}\n"

    if not pd.isna(hardskills):
        job_profile += f"Hard Skills: {preprocess_text(hardskills)}\n"

    return job_profile
