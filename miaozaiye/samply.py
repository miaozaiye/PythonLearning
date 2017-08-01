#无放回抽样


import random
import sys

#get the sample number and total list number


# m = int(input('please input the total number of List:'))
# n = int(input('please input number of sample:'))

# 创建随机列表

def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    List = [i for i in range(m)]
    print(List)
    sample = []
    for i in range(n):
        index = random.randrange(m-i)
        print('index is {0}'.format(index))
        sample.append(List[index])
        List.pop(index)

    print (sample)


main()