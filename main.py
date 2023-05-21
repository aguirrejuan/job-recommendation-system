from recomendation_system import get_list_jobs
from json_models import UserInfo, JobDetails
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_job_details", response_class=HTMLResponse)
def get_job_details(user_info: UserInfo):
    # Process the user information and retrieve multiple job details

    job_list = get_list_jobs(user_info)
    return templates.TemplateResponse("job_details.html", {"job_list": job_list})
