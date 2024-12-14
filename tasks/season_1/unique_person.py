from datetime import datetime

CURRENT_DATE = datetime(2018, 1, 1)


class Person:
    def __init__(self, first_name, last_name, birth_date,
                 job, working_years, salary, country, city, gender='unknown'):

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self) -> str:
        # return self.first_name + " " + self.last_name
        # return "%s %s" % (self.first_name, self.last_name)
        # return "{} {}".format(self.first_name, self.last_name)
        # return f"{self.first_name} {self.last_name}"
        # pattern = "{} {}"
        # return pattern.format(self.first_name, self.last_name)
        pattern = "{name} {last}"
        return pattern.format(last=self.last_name, name=self.first_name)

    def age(self) -> int:
        years_delta = CURRENT_DATE.year - self.birth_date.year
        if CURRENT_DATE.month < self.birth_date.month or \
                CURRENT_DATE.day < self.birth_date.day:
            years_delta -= 1
        return years_delta

    def money(self) -> str:
        # return "{:_}".format(self.salary * self.working_years * 12).replace("_", " ")
        # return format(self.salary * self.working_years * 12, "_").replace("_", " ")
        # return format(self.salary * self.working_years * 12, "_").replace("_", " ")
        # return format(self.salary * self.working_years * 12, "_").replace("_", " ")
        return format(self.salary * self.working_years * 12, "_").replace("_", " ")

    def work(self) -> str:
        prefix = "Is"
        if self.gender == "male":
            prefix = "He is"
        elif self.gender == "female":
            prefix = "She is"
        return "{} a {}".format(prefix, self.job)

    def home(self) -> str:
        return "Lives in {city}, {country}".format(city=self.city, country=self.country)
