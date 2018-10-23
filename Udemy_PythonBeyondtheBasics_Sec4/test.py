# coding=utf-8

from calling_parent_constructor_super   import Dog

# calling parent class constructor demo
rover = Dog('Rover')

print('The dogs name is {0} and the breed is {1}'.format(rover.name, rover.breed))
rover.fetch('shoe')
