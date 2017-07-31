#人口增长模型：t,x;(t+1),rx(1-x),r取什么值， 人口可以稳定在x = 1-1/r?

'''

n = 0
x = 0.01

if x(t) = 1, break
if x(t) = 0, break
List = []
r = 0.1, step = 0.1

while true:
    while true:

        x(t) = r*x(t-1)*(1-x(t-1))
        delta =abs(x(t) - x(t-1))
        t+=1
        if x == 1:
            print x is 1
            break
        if x == 0:
            print x is 0
            break
        if delta == 0:
            print delta is 0, r is r
            break
    r +=0.1

'''

def headcount():
    r = 0.1
    while True:
        t = 1
        x = 0.01
        List = []
        # print ('r is {0}'.format(r))
        while True:

            x_0 = x
            x = r*x*(1-x)
            delta = abs(x - x_0)
            t += 1


            if x >= 1 or x <=0:
                print ('evolution stopped,\n     x is {0}, r is {1:.3}, t is {2}'.format(x,r,t))
                # print(List)
                break
            if x_0 == x:
                print('evolution balanced,\n x is{0},r is {1:.3}, t is {2}'.format(x,r,t))
                # print(List)
                break
            if x in List:
                print ('infinite loop,\n location of the same value is at {0},r is {1:.3},t is {2}'.format(List.index(x),r,t))
                break

            List.append(x)
            # print(' * '*int(x*10))

        r +=0.2


headcount()