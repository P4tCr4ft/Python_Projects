import time
import sys

print('First line of this program')

somenum = 0

while True:
    print('first line of while loop')
    cmd = sys.stdin.readline()
    cmd_find = cmd.find('blah')
    print('cmd_find is ... {} and is type {}'.format(cmd_find, type(cmd_find)))
    time.sleep(1)
    somenum += 1
    if somenum == 8:
        print('somenum is ...{}'.format(somenum))
        break
    else:
        continue