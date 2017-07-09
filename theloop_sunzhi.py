#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#conditional statement

birth = 1990

if birth < 2000:
    print('00前')
else:
    print('00后')

#loop statement

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print('hello ' + l)
i = [1,2,3,4,5]
sum = 0
for x in i:
    sum += x
print(sum)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)



#dict

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Bob'] = 100
print(d['Bob'])