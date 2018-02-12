#整理出某篇文章各个单词的频率，并排序
'''
1. 输入文章内容
2。读取文章内容并排序
3。在已排好序的列表内，读取每个单词及其出现的频率，用 wordcount 类

'''

import sys
from miaozaiye import merge

class wordcount():
    def __init__(self,word):
        self.word = word
        self._count = 1

    def increment(self):
        self._count+=1

    def count(self):
        return self._count

def count(List):
    zipf = {}
    countlist = []
    for i in range(len(List)):
        if List[i] != List[i-1]:
            word=wordcount(List[i])
            zipf[List[i]]=word
        zipf[List[i]].increment()

    for word in zipf.keys():
        countlist.append((word,zipf[word].count()))

    return countlist



def cleandata(fh,List):
    non_use=',.?!:;()\n""-'
    non_use_word=['a','is','to','this','that','and','-','you','in']

    for l in fh:
        L = []

        l = l.split(' ')
        print('this is l after strip" ":',l)
        for i in l:

            if i in['\n','"-\n','-'] or i in non_use_word:
                pass
            else:
                i = i.rstrip(non_use).lstrip(non_use)
                L.append(i)
                print(L)

        List +=L

    print('List is:',List)
    return List

def main():
    List = []
    #1 clean the paragraph into word list
    fh = open('/Users/Jane/Desktop/PythonLearning/miaozaiye/article',mode='r')
    List=cleandata(fh,List)

    #2 sort the list

    List = merge.insert(List)

    #3 count the word
    List_after_count= count(List)

    #4 sort by frequency
    '''
    实例3:对第二个关键字排序

    >>>L = [('b',6),('a',1),('c',3),('d',4)]

    >>>L.sort(lambda x,y:cmp(x[1],y[1]))

    >>>L

    >>>[('a', 1), ('c', 3), ('d', 4), ('b', 6)]
    '''
    List_after_sort = List_after_count.sort(key = lambda x:x[1],reverse=True)
    print(List_after_count)

main()