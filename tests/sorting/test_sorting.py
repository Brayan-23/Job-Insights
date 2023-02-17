from src.pre_built.sorting import sort_by
from datetime import date


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 10, "max_salary": 11, "date_posted": date.today()},
        {"min_salary": 20, "max_salary": 30, "date_posted": date.today()},
        ]
    sort_by(jobs, 'max_salary')
    assert jobs[0] == ({
        "min_salary": 20,
        "max_salary": 30,
        "date_posted": date.today()
    })
