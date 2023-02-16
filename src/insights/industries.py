from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    list_industries = []
    for type in jobs:
        if not type["industry"] in list_industries and type["industry"] != '':
            list_industries.append(type["industry"])

    return list_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return_jobs = []
    for job in jobs:
        if job.get('industry') == industry:
            return_jobs.append(job)

    return return_jobs
