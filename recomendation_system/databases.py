import chromadb
from chromadb.config import Settings
import pandas as pd
from .preprocessing_text import job_preprocessing
from tqdm import tqdm 
import yaml

# Read the YAML file
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Iterate over the paths and print the name and path

CHROMA_FOLDER = config['chroma_folder']
VACANTES_CSV = config['vacantes_csv']


def initialize_or_get_data_chroma():
    settings = Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=CHROMA_FOLDER
    )

    chroma_client = chromadb.Client(settings)

    collection = chroma_client.get_or_create_collection(
        name="recomendation_system",
        metadata={"hnsw:space": "cosine"}
    )
    return collection


def populate_chroma(collection):
    job_data = pd.read_csv(VACANTES_CSV)

    jod_data_promt = job_data.apply(
        lambda x: (x[0], job_preprocessing(*x[1:])),
        axis=1)

    for job_string in tqdm(jod_data_promt):
        collection.add(
                    documents=[job_string[1]],
                    metadatas=[{"source": "job"}],
                    ids=[str(job_string[0])]
                         )


def query_job_info(id_job):
    id_job = int(id_job)
    job_data = pd.read_csv(VACANTES_CSV)
    return job_data.query('id_vacancy == @id_job')
