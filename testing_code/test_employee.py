# Dylan Nelson
# June 02, 2024
# test_employee.py

import pytest
from employee import Employee

@pytest.fixture
# must name the fixture the same as the variable passed into the test methods, 
# so that pytest can find it.
def employee():
    employee = Employee("Dylan", "Nelson", 70000)
    return employee

def test_give_default_raise(employee):
    salary = employee.give_raise()
    assert 75000 == salary

def test_give_custom_raise(employee):
    salary = employee.give_raise(10000)
    assert 80000 == salary
