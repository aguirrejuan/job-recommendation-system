from pydantic import BaseModel


class UserInfo(BaseModel):
    country: str
    area: str
    subareas: str
    degrees: str
    wage_aspiration: float
    currency: str
    current_wage: float
    change_cities: bool
    language: str
    years_experience: int
    months_experience: int
    wish_role_name: str
    work_modality: str
    hardskills: str


class JobDetails(BaseModel):
    area: str
    work_modality: str
    country: str
    city: str
    remote: bool
    vacancy_name: str
    description: str
