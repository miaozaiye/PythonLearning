#一种随机队列数据类型，有以下几种方法
# 1- RandomQueue() 创建一个新的随机队列
# 2- q.isEmpty() 随机队列是否为空
# 3- q.enqueue(item) 将item加入到随机队列中
# 4- q.dequeue()移除一个随机项目
# 5- q.sample()返回一个随机项目但不删除
# 6- len(q) 随机队列q中项目个数


import sys
sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')

from stdpackage import stdrandom

class RandomQueue:
    def __init__(self):
        '''

        :param n:
        :return: random queue with n items
        '''

        self._queue = []


    def queue(self):
        return self._queue

    def isEmpty(self):
        '''

        :return: True if len(self._queue) is 0
        '''
        return len(self._queue) is 0

    def enqueue(self,item):
        '''

        :param item:
        :return: append item at the end of queue
        '''

        self._queue.append(item)
        return self._queue

    def dequeue(self):
        '''

        :return: dequeue a random item in queue
        '''
        n = len(self._queue)
        i = int(stdrandom.uniformInt(0,n-1))

        if i != n-1:
            print('i is {0}'.format(i))
            self._queue[i],self._queue[-1] = self._queue[-1],self._queue[i]
            print('last item is{0}'.format(self._queue[-1]))
        n = self._queue.pop(-1)

        return n

    def sample(self):
        n = len(self._queue)
        i = int(stdrandom.uniformFloat(0,n))
        return self._queue[i]

def main():
    n = sys.argv[1]
    q = RandomQueue(n)
    print('generate randomqueue:\n',q.queue())
    print('check if is empty:',q.isEmpty())
    print('get a sample: ',q.sample())
    item = int(input('enqueue an item:'))

    q.enqueue(item)
    print('new queue is:\n',q.queue())

    print('run dequeue...,pop{0} '.format(q.dequeue()),q.queue())



if __name__ == '__main__': main()