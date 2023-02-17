from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salary = 0
    for type in jobs:
        if type.get('max_salary') == '':
            max_salary = max_salary
        elif type["max_salary"] != 'invalid' and \
                max_salary < int(type['max_salary']):
            max_salary = int(type["max_salary"])

    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salary = get_max_salary('data/jobs.csv')
    for type in jobs:
        if type.get('min_salary') == '':
            min_salary = min_salary
        elif type["min_salary"] != 'invalid' and \
                min_salary > int(type['min_salary']):
            min_salary = int(type["min_salary"])

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError
    elif (
        isinstance(job.get('min_salary'), int) is False
        or isinstance(job.get('max_salary'), int) is False
    ):
        raise ValueError
    elif int(job.get("min_salary")) > int(job.get("max_salary")):
        raise ValueError
    elif (
        isinstance(salary, int) is False
        and isinstance(salary, str) is False
    ):
        raise ValueError

    result = int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])

    return result


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
