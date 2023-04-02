"""
modify the Animal class so that:
- The `Animal` class can no longer be instantiated.
- Any subclass of `Animal` class must have a `get_favourite_food()` method
    so that the `hungry()` method can remain consistent.
remember to import proper packages here
"""
from abc import ABC, abstractmethod

# modify the Animal class
class Animal(ABC):
    def hungry(self):
        print('I want to eat {}!'.format(self.get_favourite_food()))

    @abstractmethod
    def get_favourite_food(self): pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_favourite_food(cls):
        return 'eggs'


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_favourite_food(cls):
        return 'milk'


zephy = Dog("Zephy")
mochi = Cat("Mochi")

zephy.hungry()
mochi.hungry()