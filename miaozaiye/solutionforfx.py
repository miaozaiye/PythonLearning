#f(x) 是一个单调递增函数，f(a)<0, f(b)>0, 求 X 使得 f(x) == 0

'''

0. f 可以是传递进来的任意一个单调递增函数，同时传递a使得f(a)<0, b ~ f(b)>0
1. 以0为搜索目标，在[a,b)中搜索满足0 对应的X值是多少
3。 因为 f 单调递增，因此可以理解为有序数列，可以直接采取二分查找法

'''


def f1(x):
    return 2*x+5


def solution(f,a,b):
    print('lo,hi:',a,b)
    lo = a
    hi = b
    mid = (a+b)/2

    if abs(f(mid) - 0) < 10**(-5):
        print('mid is:',mid)
        return mid

    elif f(mid) <0:
        solution(f,mid,hi)
    else:
        solution(f,lo,mid)



a = solution(f1,-3,1)

print(a)



