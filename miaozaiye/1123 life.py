#life game
'''
scale: 10*10

1。 在不满足状态变化条件时，保持状态不变（生，死）
2。 状态变化条件：
    1 - 周围>3个都是生，本身是生，则死。
    2 - 周围3个是死，本身是死，则生。
    3 - 一个sheng细胞，周围只有1个生细胞，则si。

    周围，只以该细胞为中心的九宫格范围。

'''
from stdpackage import stdarray,stddraw,stdrandom




def initiate(life,n):
    '''
    create original life block in central(5,5), with n alive block
    :param life:
    :return:
    '''

    life[3][5]=1
    life[4][6]=1
    life[5][4]=1
    life[5][5]=1
    life[5][6]=1
    return life


def isalive(life,x,y):
    '''
    check the surviving condition, and return True/False for alive/dead

    :param x:
    :param y:
    :return:
    '''
    print(' call isalive({0},{1})'.format(x,y))
    alive = 0
    dead = 0



    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i <0 or i>9 or j<0 or j>9:
                pass
            elif i == x and j == y:
                pass
            else:
                if life[i][j] == 1:
                    alive +=1
                elif life[i][j]== 0:
                    dead +=1

    print('item = {2},alive = {0},dead = {1}'.format(alive,dead,life[x][y]))
    if life[x][y] == 1 and alive >3:
        print(x,y,'False')
        return 0
    if life[x][y] == 0 and alive ==3:

        print(x,y,'True')
        return 1
    if life[x][y] == 1 and alive == 1:
        print(x,y,'False')
        return 0

    print('{1} {2} return {0}'.format(life[x][y],x,y))
    return life[x][y]

def draw(life):
    for i in range(len(life)):
        for j in range(len(life)):
            if life[j][i] == 1:
                stddraw.filledSquare(i,10-j-1,0.5)


def lifegame(life):
    '''
    recursive return the adjacent part block

    :param x:
    :param y:
    :return:
    '''
    stddraw.clear()
    draw(life)
    stddraw.show(500)
    for line in life:
        print(line)

    life2 = stdarray.create2D(10,10,0)
    for x in range(10):
        for y in range(10):
            print('x is {0},y is {1}'.format(x,y))

            a = 0
            for i in range(x-1,x+2):
                # print('i is {0}'.format(i))
                for j in range(y-1,y+2):
                    # print('j is {0}'.format(j))
                    if i <0 or i>9 or j<0 or j>9:
                        pass
                    else:

                        a +=life[i][j]
                        print('i is {0},j is {1},life[{0}][{1}] is {3},a is{2}'.format(i,j,a,life[i][j]))

            if a == 0:
                print(x,y,'no alive in 9')
                pass
            else:

                life2[x][y] = isalive(life,x,y)

    lifegame(life2)





def main(n):
    life = stdarray.create2D(10,10,0)
    stddraw.setXscale(-1,10)
    stddraw.setYscale(-1,10)
    life = initiate(life,n)
    lifegame(life)

main(5)






