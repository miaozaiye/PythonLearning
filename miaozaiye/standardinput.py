import sys
import math

def main():
    s = sys.argv[1:]
    x = int(s[0])
    y = int(s[1])
    z = int(s[2])
    r = 0

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        s = line.split(',')
        x_1 = int(s[0])
        y_1 = int(s[1])
        z_1 = int(s[2])

        r_1 = math.sqrt((x-x_1)*(x-x_1) + (y-y_1)*(y-y_1) +(z-z_1)*(z-z_1))
        if r_1>r:
            r = r_1
            x_0 = x_1
            y_0 = y_1
            z_0 = z_1
        else:
            pass

        print('r is {0:.2f},(x,y,z) is {1}'.format(r,(x_0,y_0,z_0)))

main()