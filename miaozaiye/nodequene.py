#通过链表的方式来建立FIFO的队列
'''
1。 建立NODE类型
2。 建立链表类型：
    1）第一个元素
    2）最后一个元素
    3）每加入一个元素，都加入到最后一个元素的 Next
    4）每推出一个元素，都从第一个推出，解链，返回第一个。
'''


import sys
sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')
sys.path.insert(0,'/Users/Jane/Desktop/PythonLearning')

class _node():
    def __init__(self,item):
        self.item = item
        self.next = None


class link():
    def __init__(self):
        self.last = None
        self.first = None
        self._n = 0


    def inqueue(self,item):
        newlast = _node(item)
        oldlast = self.last
        self.last = _node(item)
        if self.isempty():self.first=self.last
        else: oldlast.next = self.last
        self._n +=1

    def outqueue(self):
        first = self.first.item
        self.first = self.first.next
        return first

    def isempty(self):

        return not self.first


def main():
    L = 'to be or not to be - - - -'

    L1 = L.split(' ')
    L2 = link()
    print(L1)
    for l in L1:
        if l!= '-':
            L2.inqueue(l)
        else:
            print(L2.outqueue())


# main()