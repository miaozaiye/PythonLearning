import struct
import datetime



Contact = struct.Struct('<15si')

list = []

l1 = Contact.pack('Abe Baker'.encode('utf8'),762)

print(l1)

l2 = Contact.pack('Cindy Dove'.encode('utf8'),987)

print ('length is {0}'.format(len(l2)))

u1 = Contact.unpack(l1)[0].decode('utf8').rstrip(chr(0))

print('u1 is {0}'.format(u1))

import time

def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime-startTime)*1000
        print ('->elapsed time: %f ms'%msecs)

    return wrapper

@deco
def myfunc():
    print ('start mufunc')
    time.sleep(0.6)
    print ('end myfunc')

print('myfunc is:',myfunc.__name__)
myfunc()

@deco
def newfunc():

   a =  [i for i in range(1000)]
   print (a)
   return a

newfunc()