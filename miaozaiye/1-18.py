#excercise of 1-18
#given a group of real number in range(-1,1), calculate the average(abs(x)), abs(x)**, and the cross-0 times.

#can both read number from standard input or from saved file.

import math
import random
import sys

def calculate(x_list):
    assert len(x_list)>0,'division by zero'
    x_abs = [abs(x) for x in x_list]
    x_average = sum(x_abs)/len(x_abs)
    x_f = [x*x for x in x_abs]
    x_0 = 0
    x_cross = 0
    for x in x_list:
        x_cross +=1 if x*x_0 <0 else 0
        x_0 = x

    return (x_average,x_f,x_cross)

def main():


    print('please input the real number in range(-1,1)')
    x_list = []
    while True:
        try:
            number = float(sys.stdin.readline())
            if number < -1 or number >1:
                print('your input is out of range, please input again.\n')
            else:
                x_list.append(number) if isinstance(number,float) else 'end'
        except ValueError:
            print(ValueError)
            break
    x_average,x_f,x_cross = calculate(x_list)

    print(x_average,x_f,x_cross)

main()