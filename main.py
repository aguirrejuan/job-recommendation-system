from recomendation_system import get_list_jobs
from json_models import UserInfo, JobDetails
from fastapi import FastAPI
from typing import List


app = FastAPI()


@app.post("/get_job_details")
def get_job_details(user_info: UserInfo) -> List[JobDetails]:
    job_list = get_list_jobs(user_info)
    return job_list
