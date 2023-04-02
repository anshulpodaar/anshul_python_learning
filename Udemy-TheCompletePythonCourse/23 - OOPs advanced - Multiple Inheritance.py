"""
Define your Salary class and Promotable class so that the Employee class objects may work like this:
rolf = Employee(15.0)
print(rolf.weekly_salary())     # --> prints out rolf's weekly salary (15.0 * 40 = 600.0)
rolf.promote(5.0)       # rolf's hourly salary (rate) increases by 5.0 (15.0 + 5.0 = 20.0)
print(rolf.weekly_salary())     # --> prints 800.0  (20.0 * 40 = 800.0)
"""


class Salary:
    # define Salary class and associated methods here
    def calculate(self, hours: float) -> float:
        return self.rate * hours



class Promotable:
    # define Promotable class and associated methods here
    def promote(self, _raise: float) -> None:  # _raise so it doesn't clash with Python's raise keyword!
        self.rate += _raise
        return None


# Do NOT change the code below:
class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate

    def weekly_salary(self) -> float:
        return self.calculate(40)


rolf = Employee(15.0)
print(rolf.weekly_salary())
rolf.promote(5.0)
print(rolf.weekly_salary())