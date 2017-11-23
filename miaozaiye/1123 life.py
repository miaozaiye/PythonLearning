#life game
'''
scale: 10*10

1。 在不满足状态变化条件时，保持状态不变（生，死）
2。 状态变化条件：
    1 - 周围3个都是生，本身是生，则死。
    2 - 周围超过3个是死，本身是死，则生。
    3 - 一个死细胞，周围只有1个生细胞，则生。

    周围，只以该细胞为中心的九宫格范围。

'''
from stdpackage import stdarray,stddraw,stdrandom

global life
life = stdarray.create2D(10,10,False)

def initiate(life,n):
    '''
    create original life block in central(5,5), with n alive block
    :param life:
    :return:
    '''
    life[4][5]=True
    life[4][6]=True
    life[5][7]=True
    life[7][7]=True

    return life


def isalive(x,y):
    '''
    check the surviving condition, and return True/False for alive/dead

    :param x:
    :param y:
    :return:
    '''
    alive = 0
    dead = 0
    for i in range(x-1):
        for j in range(y-1):
            if i == x and j == y:
                pass
            else:
                if life[i][j] == True:
                    alive +=1
                else:
                    dead +=1
    if life[x][y] == True and alive >=3:
        print(x,y,'False')
        return False
    if life[x][y] == False and (dead >=3 or alive ==1):
        return True
        print(x,y,'True')



    return life[x][y]

def draw(life):
    for i in range(len(life)):
        for j in range(len(life)):
            if life[i][j]:
                stddraw.filledSquare(i,10-j-1,0.5)


def lifegame(x,y):
    '''
    recursive return the adjacent part block

    :param x:
    :param y:
    :return:
    '''
    stddraw.clear()


    if x < 0 or x > 10 or y < 0 or y > 10:
        return

    life[x][y] = isalive(x,y)
    draw(life)
    stddraw.show(200)


    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            print('i is {0},j is {1}'.format(i,j))
            if i == x and j == y:
                print('i ==x and j == y',i,j)
                pass
            else:
                print('enter next layer',i,j)
                lifegame(i,j)




def main(n):
    stddraw.setXscale(-1,11)
    stddraw.setYscale(-1,11)

    life[4][5]=True
    life[4][6]=True
    life[5][6]=True
    life[7][7]=True

    lifegame(5,5)

main(5)






