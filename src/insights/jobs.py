from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8", mode="r") as file:
        jobs = csv.DictReader(file, delimiter=",")
        list = []
        for job in jobs:
            list.append(job)
    return list


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    list_types = []
    for type in jobs:
        if not type["job_type"] in list_types:
            list_types.append(type["job_type"])

    return list_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return_jobs = [job for job in jobs if job["job_type"] == job_type]

    return return_jobs
