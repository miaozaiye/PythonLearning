#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[len(classmates)-1])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

classmates.append('Adam')
print(classmates.__len__())
print(len(classmates))
print(classmates)

print(classmates.pop())
print(classmates)
print(classmates.pop(1))
print(classmates)
classmates[1] = 'Sarah'
print(classmates)

L = ['Apple', 123, True]

print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']

print(s)
print(len(s))

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][1])
