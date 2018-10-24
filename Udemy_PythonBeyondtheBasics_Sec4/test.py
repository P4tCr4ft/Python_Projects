# coding=utf-8

from calling_parent_constructor_super   import Dog, Puppy, Runt
from static_and_class_methods_decorators import InstanceCounter, InstanceCounter2


# calling parent class constructor demo
# rover = Dog('Rover')
# rover = Puppy('Rover', 2)
rover = Runt('Rover', 2)

# print('The dogs name is {0} and the breed is {1}'.format(rover.name, rover.breed))
# print('The dogs age is {0}'.format(rover.age))
rover.fetch('shoe')
print()




# static and class methods, and decorator example

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print('value of obj: {}'.format(obj.get_val()))# initialised values in constructor, 5, 13, etc)
    print('Instance count: {}'.format(obj.get_count()))# is always 3

print()

d = InstanceCounter2(9)
e = InstanceCounter2(19)
f = InstanceCounter2('hi')# staticmethod validity check returns zero, as non integer passed in

for obj in (d, e, f):
    print('value of obj: {}'.format(obj.get_val()))# initialised values in constructor, 5, 13, etc)
    print('Instance count: {}'.format(obj.get_count()))# is always 3

