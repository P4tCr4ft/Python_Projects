from assignments_steve                  import MaxSizeList

from calling_parent_constructor_super   import Dog

a = MaxSizeList(3)
b = MaxSizeList(1)
c = MaxSizeList('oops')
d = MaxSizeList('7')
print('Got to line 7')

# a.push('')
a.push(0)
a.push('hey')
a.push('hi')
a.push('lets')
a.push('go')
print('got to line 13')

b.push('hey')
b.push('hi')
b.push('lets')
b.push('go')
print('got to line 19')

c.push('hey')

c.push('hey')
print('got to line 24')

print(a.get_list())
print(b.get_list())


rover = Dog('Rover')

print('The dogs name is {0} and the breed is {1}'.format(rover.name, rover.breed))
rover.fetch('shoe')


print('this is last line')