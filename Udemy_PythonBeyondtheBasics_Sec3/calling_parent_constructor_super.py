# coding=utf-8

import random

class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        # Python 2 syntax below, needs class which you're calling parent of, and the Dog object, self
        # super(Dog, self).__init__(name)

        # Python 3 syntax is simpler
        super().__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print('{0} ran and fetched the {1}'.format(self.name, thing))