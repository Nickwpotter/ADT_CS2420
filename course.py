''' Course Class for Project 4 of CS 2420 '''
from slist import SList

class Course:
    ''' Course object '''
    def __init__(self, number: int = 1, name: str = '', credit_hour:float = 3.0, grade: float or int = 2.0):
        self.crs_number = number
        self.crs_name = name
        self.credit_hour = credit_hour
        self.crs_grade = grade
        try:
            if not isinstance(number, int) or number < 0:
                raise ValueError('number is the wrong type or inappropriate value')
            if not isinstance(name, str):
                raise ValueError('name is the wrong type')
            if not isinstance(credit_hour, float) or credit_hour <= 0:
                raise ValueError('credit_hour is the wrong type')
            if not isinstance(grade, float or int) or (grade < 0.0 or grade > 4.0):
                raise ValueError('grade is the wrong type or inappropriate value')
        except ValueError as e:
            raise e


    def number(self):
        return self.crs_number

    def name(self):
        return str(self.crs_name)
    
    def credit_hr(self):
        return float(self.credit_hour)
    
    def grade(self):
        return self.crs_grade
    
    def __eq__(self, other):
        course = other
        if isinstance(other, Course):
            course = other.crs_number
        return self.crs_number == course
    
    # def __ne__(self, other):
    #     course = other
    #     if isinstance(other, Course):
    #         course = other.number()
    #     return self.number() != course
    
    def __lt__(self, other):
        course = other
        if isinstance(other, Course):
            course = other.crs_number
        return self.crs_number < course    
    
    # def __gt__(self, other):
    #     course = other
    #     if isinstance(other, Course):
    #         course = other.number()
    #     return self.number() > course
      
    def __le__(self, other):
        course = other
        if isinstance(other, Course):
            course = other.crs_number
        return self.crs_number <= course
    
    # def __ge__(self, other):
    #     course = other
    #     if isinstance(other, Course):
    #         course = other.number()
    #     return self.number() >= course
    
    def __str__(self, other):
        return f'cs{self.number()} {self.name()} Grade:{self.grade()} Credit Hours: {self.credit_hr()}'