from .json_models import UserInfo, JobDetails
from typing import List
from .databases import initialize_or_get_data_chroma, query_job_info
from .preprocessing_text import user_preprocessing


def get_list_jobs(user_info: UserInfo) -> List[JobDetails]:

    collection = initialize_or_get_data_chroma()
    user_preprocessing_promt = user_preprocessing(**user_info.dict())

    job_list_matchs = collection.query(
        query_texts=[user_preprocessing_promt],
        n_results=5, include=['distances'])

    ids = job_list_matchs['ids'][0]
    distances = job_list_matchs['distances'][0]

    job_list = []
    for id_, dist in zip(ids, distances):
        job_dict = query_job_info(id_).to_dict('records')[0]
        job_list.append(JobDetails(**job_dict, match_score=dist))

    return job_list
