#!usr/bin/Python 
#!-*- coding=utf-8 -*-

def deque(items):
    #这个去除重复项的函数只对能够hash的对象有效，数据，字符串，元组都是可以hash的对象
    seen = set()
    for item in items:
        if item not in seen:
             yield item
             seen.add(item)

def dedupe(items,key=None):
    #扩展一个通用的去重复的函数
    #通过key函数来对不可hash的对象进行hash化处理
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

