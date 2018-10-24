# coding=utf-8

import random

class Animal(object):
    def __init__(self, name):
        print('Animal constructor')
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        print('Dog constructor')
        # Python 2 syntax below, needs class which you're calling parent of, and the Dog object, self
        # super(Dog, self).__init__(name)

        # Python 3 syntax is simpler
        super().__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print('{0} ran and fetched the {1}'.format(self.name, thing))


class Puppy(Dog):
    def __init__(self, name, age):
        print('Puppy constructor')
        super(Dog, self).__init__(name)
        self.age = age


# Can specify calling the constructor of the primary child class Dog, which
# actually skips calling the constructors of those in the hierarchy between Runt and Dog
class Runt(Puppy):
    def __init__(self, name, age):
        print('Runt constructor')
        super(Dog, self).__init__(name)
        self.risk_factor = 10