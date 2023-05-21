# <center> Job Recomendation System <center/>



## Installation


Clone the repository
```
pip install -r requirements.txt
```



### Example: 

```
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
    "hardskills": "HTML, CSS, JavaScript"
}' http://localhost:8000/get_job_details
```