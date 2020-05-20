from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('', 16000))
timestr = time.ctime(time.time()) + "\r\n"
s.send(timestr.encode('ascii'))
returntime = s.recv(8192)
s.close()
print('Return time is ... {}'.format(returntime.decode('ascii')))
