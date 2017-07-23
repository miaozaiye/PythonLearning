#利用蒙特卡洛模拟赌徒概率

'''
sum : 一次模拟中累计的资金数，刚开始模拟时则是启动资金数
bet:每次下注的金额（赢了则获得同等数量金额，输了则失去同等数量金额）
target:期望账户累计到多少金额就不玩了，默认账户为0就不玩了
trials: 模拟的次数

期望结果：
在模拟次数中，胜出的比例是多少。
每次胜出，用了多少次，平均数／最大数／最小数／中位数如何

'''
import random
import optparse

def gambler(sum_start,bet,target,trials):

    win_trial = []

    for t in range(trials):
        _sum = sum_start

        times = 0
        times_win = 0
        while _sum >0 and _sum <target:
            result = bet if random.randrange(0,2)>0 else -bet
            _sum += result
            times+=1

        if _sum >= target:
            win_trial.append((times,_sum))



    print('total {0} times win, ratio is {1}'.format(len(win_trial),len(win_trial)/trials))

    l1 = [t for t,s in win_trial] #获得所有胜出模拟中，投注的次数
    average = int(sum(l1)/len(l1)) #获得平均胜出投注次数
    max_num = max(l1)
    min_num = min(l1)
    mid_num = l1[int(len(l1)/2)] if (len(l1)/2)%2 == 1 else (l1[int(len(l1)/2)] + l1[int(len(l1)/2)-1])/2

    print('average is {0}, max_num is {1},min_num is {2},mid_num is {3}'.format(average,max_num,min_num,mid_num))


def main():
    parser = optparse.OptionParser("""\
usage: %prog [options] infile outfile

simulate the gamble result: how many times you will win, what's the possibility,
average, max, min & middle number of bets""")

    parser.add_option("-b", "--bet", dest="bet",
            help=("input the sum_start,bet,target,trials"))
    opts, args = parser.parse_args()

    sum_start,bet,target,trials = opts.bet.split(',')


    gambler(int(sum_start),int(bet),int(target),int(trials))

main()