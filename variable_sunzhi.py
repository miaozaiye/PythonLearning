# print absolute value of an integer:
a=-100
if(a>0):
    print(a)
else:
    print(-a)

print('I\'m ok.')

#Not escaped
print(r'\\\t\\')
#escaped
print('\\\t\\')

#boolean
print(3>2)

#print variable
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(s2)
print(s3)
print(s4)

a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(a)
