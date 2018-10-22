from assignments_steve import MaxSizeList

a = MaxSizeList(3)
b = MaxSizeList(1)
c = MaxSizeList('oops')
d = MaxSizeList('7')
print('Got to line 7')

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
print('this is last line')