import struct

Contact = struct.Struct('<15si')

list = []

l1 = Contact.pack('Abe Baker'.encode('utf8'),762)

print(l1)

l2 = Contact.pack('Cindy Dove'.encode('utf8'),987)

print ('length is {0}'.format(len(l2)))

u1 = Contact.unpack(l1)[0].decode('utf8').rstrip(chr(0))

print('u1 is {0}'.format(u1))