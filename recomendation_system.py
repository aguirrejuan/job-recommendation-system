
from json_models import UserInfo, JobDetails
from typing import List


def get_list_jobs(user_info: UserInfo) -> List[JobDetails]:
    job_list = [
        JobDetails(
            area=user_info.area,
            work_modality=user_info.work_modality,
            country=user_info.country,
            city="Example City 1",
            remote=True,
            vacancy_name="Software Engineer",
            description="An exciting opportunity for an experienced Software Engineer.",
        ),
        JobDetails(
            area=user_info.area,
            work_modality=user_info.work_modality,
            country=user_info.country,
            city="Example City 2",
            remote=False,
            vacancy_name="Data Scientist",
            description="Join our team as a Data Scientist and work on cutting-edge projects.",
        ),
    ]
    return job_list
