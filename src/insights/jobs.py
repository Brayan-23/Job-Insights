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
    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    list_types = []
    for type in jobs:
        if not type["job_type"] in list_types:
            list_types.append(type["job_type"])

    return list_types

    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
