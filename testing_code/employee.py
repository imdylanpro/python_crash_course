# Dylan Nelson
# June 02, 2024
# employee.py

class Employee:
    '''Represents an individual employee with a first name, last name, and 
    salary.'''

    def __init__(self, first_name, last_name, salary):
        '''Assigns the characteristics of name and salary to the employee.'''
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salay_raise=5000):
        '''Increases the salary of the employee by 5000 by default or a 
        specified value.'''
        self.salary += salay_raise
        salary = self.salary
        return salary
