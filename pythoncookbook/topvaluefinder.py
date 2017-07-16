#!/usr/bin/python

import  heapq

num={1,3,5,7,7,2,-23,42,47,56,83,-90}

print(heapq.nlargest(3,num))
print(heapq.nsmallest(3,num))


#print(heap.nlargest(3,nums))

portfolio = [{'name':'IBM','share':100,'price':101.1},
            {'name':'AMZ','share':90,'price':991.1},
             {'name':'GOL','share':700,'price':1091.1},
            {'name':'MIC','share':190,'price':91.1},
            {'name':'APP','share':1010,'price':96.1},
            {'name':'Yah','share':900,'price':97.1},]
cheap = heapq.nsmallest(3,portfolio,key=lambda x: x['price'])
expensive = heapq.nlargest(3,portfolio,key=lambda x: x['price'])
print cheap
print expensive

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
       print priority
       heapq.heappush(self._queue,(-priority,self._index,item))
       self._index +=1

    def pop(self):
        print 'Pop once'
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Item({!r})".format(self.name)


q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)

q.pop()
q.pop()
q.pop()

