import sys
import math

def main():
    s = sys.argv[1:]
    x = int(s[0])
    y = int(s[1])
    z = int(s[2])
    r = 0
    List = []
    while True:
        line = sys.stdin.readline()

        if not line:
            break
        s = line.split(',')
        print('this is s:{0}'.format((s[0],s[1],s[2].rstrip())))
        x_1 = int(s[0].rstrip())
        y_1 = int(s[1])
        z_1 = int(s[2].rstrip())

        r_1 = math.sqrt((x-x_1)*(x-x_1) + (y-y_1)*(y-y_1) +(z-z_1)*(z-z_1))
        List.append((r_1,x_1,y_1,z_1))

    print(List)
    sorted(List,lambda x:x[0])
    print(List)


main()