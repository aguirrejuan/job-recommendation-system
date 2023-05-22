# Job Recommendation System

This repository contains a job recommendation system built with FastAPI and Chroma upon LLMs (Large Language Models). It allows users to input their information and receive personalized job recommendations based on their preferences.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/aguirrejuan/job-recommendation-system.git
   ```

2. Navigate to the project directory:

   ```shell
   cd job-recommendation-system
   ```

### Running with Docker

1. Build the Docker image:

   ```shell
   docker build -t job-recommendation-system .
   ```

2. Run the Docker container:

   ```shell
   docker run -d --name job-recommendation-container -p 8000:8000 job-recommendation-system
   ```

   The FastAPI server will start inside the Docker container and listen on `http://localhost:8000`.

### Running without Docker

1. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

2. Start the FastAPI server:

   ```shell
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   The server will start and listen on `http://localhost:8000`.

## Usage

To use the job recommendation system, follow these steps:

1. Send a POST request to the `/get_job_details` endpoint with the required information. You can use tools like cURL or Postman to make the request.

   Here's an example using cURL:

   ```shell
   curl -X POST -H "Content-Type: application/json" -d '{
       "country": "USA",
       "area": "Software Development",
       "subareas": "Web Development",
       "degrees": "Computer Science",
       "wage_aspiration": 80000.0,
       "currency": "USD",
       "current_wage": 60000.0,
       "change_cities": true,
       "language": "Python",
       "years_experience": 3,
       "months_experience": 6,
       "wish_role_name": "Full Stack Developer",
       "work_modality": "Remote",
       "hardskills": ["HTML", "CSS", "JavaScript"]
   }' http://localhost:8000/get_job_details
   ```

   Adjust the request payload to match your preferences and requirements.

2. The server will process the request and return a list of job recommendations based on the provided information. An return a Json with 5 posible jobs 

```
{
  "area": "Software Development",
  "work_modality": "Remote",
  "country": "USA",
  "city": "Example City 1",
  "remote": true,
  "vacancy_name": "Software Engineer",
  "description": "An exciting opportunity for an experienced Software Engineer."
  "match_score": 0.81,
},
{
  "area": "Software Development",
  "work_modality": "Remote",
  "country": "USA",
  "city": "Example City 2",
  "remote": false,
  "vacancy_name": "Data Scientist",
  "description": "Join our team as a Data Scientist and work on cutting-edge projects."
  "match_score": 0.8,
},
{
  "area": "Web Development",
  "work_modality": "On-site",
  "country": "UK",
  "city": "Example City 3",
  "remote": false,
  "vacancy_name": "Frontend Developer",
  "description": "Looking for a skilled Frontend Developer to join our dynamic team."
  "match_score": 0.73,
},
{
  "area": "Data Analysis",
  "work_modality": "Remote",
  "country": "Germany",
  "city": "Example City 4",
  "remote": true,
  "vacancy_name": "Data Analyst",
  "description": "Exciting opportunity for a Data Analyst with strong analytical skills."
  "match_score": 0.67,
},
{
  "area": "Network Security",
  "work_modality": "On-site",
  "country": "Canada",
  "city": "Example City 5",
  "remote": false,
  "vacancy_name": "Network Security Engineer",
  "description": "Join our team and help protect our network infrastructure."
  "match_score": 0.27,
}

```

## Populate Chroma Database 

```
python populate_dataset.py
```

### Configuration of folders 
 YAML file has the folder used to storage the CSV files and chroma embeddings
 
```
chroma_folder: "./datasets/chroma"
vacantes_csv : "./datasets/vacantes.csv"
```
