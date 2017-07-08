#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

#str format out
print('Hi, %s, you have $%d.' % ('Michael', 1000000))


s1 = 72
s2 = 85
result = 85-72/72
print("the score increases %.2f" % result)