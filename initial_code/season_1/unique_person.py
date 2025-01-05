from datetime import datetime

CURRENT_DATE = datetime(2018, 1, 1)


class Person:
    def __init__(self, first_name, last_name, birth_date,
                 job, working_years, salary, country, city, gender='unknown'):
       ...
