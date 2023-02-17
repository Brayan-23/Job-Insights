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

    try:
        max = int(job.get('max_salary'))
        min = int(job.get('min_salary'))
        salary_int = int(salary)

        if min > max:
            raise ValueError

        return min <= salary_int <= max
    except (TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    list_sucess = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                list_sucess.append(job)
        except ValueError as err:
            print(err)
    return list_sucess
