#找到输入的5个数中间的中值，寻找次数不要多于7次
'''
algorithm:

排序然后寻找中位数。

1：冒泡排序 & 寻找中位数
2：直接比较每个数，有多少个数是小于或者大于自己的。当这个数等于2，则是中位数

'''

def median(A,B,C,D,E):
    List = [A,B,C,D,E]
    n = 0
    t = 1

    for j in range(len(List)-1):
        if t >2:
            break

        else:
            for i in range(len(List)-t):
                if List[i] < List[i+1]:
                    n+=1
                    print('i is {0},List[i] is {1},List[i+1] is {2}'.format(i,List[i],List[i+1]))
                    pass
                else:
                    print('changed, i is {0},List[i] is {1},List[i+1] is {2}'.format(i,List[i],List[i+1]))
                    a = List[i]
                    List[i] = List[i+1]
                    List[i+1]=a
                    n+=1
            t+=1

    median = List[2]
    print ('n is {0},median is {1}'.format(n,median))
    print(List)



median(3,5,2,1,4)