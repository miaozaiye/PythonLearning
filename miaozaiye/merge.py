#通过归并排序算法，大大提升排序的速度。

'''
1. 二分拆解
2。 每个拆解组，单独插入排序
'''

import sys
sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')
from stdpackage import stdarray

List = [1,5,6,7,2,3,5]

#solution 2:



def merge(hi,mid,lo,List):

    x = 0
    i = lo
    j = mid
    n = hi - lo
    aux = stdarray.create1D(n,0)

    for k in range(n):

        if i == mid:aux[k]=List[j];j+=1; #i == mid,意味着[lo,mid)的数字已经排完了，接下来就是依次将 j - hi的元素排进 aux;下面的操作都不会在进行。

        elif j == hi: aux[k]=List[i];i+=1; # j == hi,意味着[mid,hi)的数字已经排完了，接下来就是依次将 i-mid的元素排进aux

        elif List[j] < List[i] : aux[k] = List[j];j+=1 #发现后半部分的元素小于前面，则排后半部分元素到当下位置。
        else: aux[k] = List[i];i+=1

    List[lo:hi] = aux[0:n]




def sort(hi,lo,List):

    if hi - lo <=1:
        return List
    mid = (hi+lo)//2
    sort(hi,mid,List)
    sort(mid,lo,List)
    merge(hi,mid,lo,List)


def insert(List):
    lo = 0
    hi = len(List)
    sort(hi,lo,List)
    return List

sort(7,0,List)

# solution 1:
# def exchange(List,j):
#     # print('exchange')
#     # print(List[j],List[j-1])
#     List[j],List[j-1] = List[j-1],List[j]
#     # print(List[j],List[j-1])
#     # print(List)
#
# def sort(List):
#     # print('sort')
#     # print(List[lo:hi])
#     lo = 0
#     hi = len(List)
#
#     for i in range(0,hi):
#         j = i
#
#         while j >lo and List[j] < List[j-1]:
#             exchange(List,j)
#
#             j-=1
#
#
# def binary(List):
#     mid = len(List)//2
#
#     if mid == 0:
#         return List
#
#     else:
#         binary(List[0:mid])
#         binary(List[mid:len(List)])
#
#
#     sort(List)
#     # print(List)
#
# binary(List)


