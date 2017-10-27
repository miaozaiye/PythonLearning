#生日问题，一个房间内随机进来多少人时，至少有两个人生日月天是一样的
'''

1：命令行输入指定月份，日期，测试次数
2： 函数1生成随机月份，日期
3： 函数2对比新的随机月份，日期，并返回结果
4： 如果结果为True，则返回人数
5： 2 - 4 循环目标次数，函数3 计算出概率分布
6： 函数4 画出概率分布密度图
'''

import random
from stdpackage import stdarray,stddraw
import  sys



possibility = stdarray.create1D(364,0)
def gen_birthday():
    print('enter gen_birthday')
    month_date = {1:[1,31],
                  2:[1,28],
                  3:[1,31],
                  4:[1,30],
                  5:[1,31],
                  6:[1,30],
                  7:[1,31],
                  8:[1,31],
                  9:[1,30],
                  10:[1,31],
                  11:[1,30],
                  12:[1,31]}
    month = random.randint(1,12)
    print(month)
    date = random.randint(month_date[month][0],month_date[month][1])
    print(date)
    return month,date

def comp_birthday(birthday1,birthday2):
    print('enter comp_birthday')
    if birthday1[0] == birthday2[0]:

        if birthday1[1] == birthday2[1]:

            print('true')
            return True
    else:
        print('false')
        return False


def rec_possibility(time):
    possibility[time] +=1

def draw_possibility():
    print('enter draw_possibility')
    stddraw.setYscale(-0.5,100)
    stddraw.setXscale(-50,400)
    for i in range(len(possibility)-1):
        stddraw.line(i,possibility[i],i+1,possibility[i+1])

    stddraw.show()

def main():
    month = int(sys.argv[1])
    date = int(sys.argv[2])
    times = int(sys.argv[3])
    month1,date1 = 0,0

    time = 0


    while sum(possibility)<times:
        count = 0
        print('loop1,count is {0},possibility_sum is {1}'.format(count,sum(possibility)))

        while count < 364:
            print('count is {0}'.format(count))
            if comp_birthday((month,date),(month1,date1)):
                print('loop4,time is {0}'.format(time))
                rec_possibility(count)
                count = 0

            count +=1

            month1,date1 = gen_birthday()
    print('possibility is {0}'.format(possibility))
    print(sum(possibility))
    draw_possibility()


main()

