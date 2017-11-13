#汉诺塔问题

'''
1。 三根柱子，n个盘子，从小到大堆叠在某根柱子上
2。 一次只能移动一个盘子，要把所有盘子都移动到另外一根柱子上
3。 大盘子不能叠加到小盘子上
4. 画出移动的动画
'''

from stdpackage import stddraw


def draw_setup(n):
    stddraw.setYscale(-1,11)
    stddraw.setXscale(-1,11)
    stddraw.line(0,-1,10,-1)
    location = {'a':(3,0,3,8),'b':(6,0,6,8),'c':(9,0,9,8)}

    stddraw.line(3,0,3,8)
    stddraw.line(6,0,6,8)
    stddraw.line(9,0,9,8)
    for i in range(1,n+2):
        print(i)
   
        stddraw.line(3-i/n,8*(n+1-i)/(n+1),3+i/n,8*(n-i+1)/(n+1))
        stddraw.text(3-i/n-0.5,8*(n-i)/n,str(i))

    return location

def draw_move(dict,a,c,location):
    print('enter move')
    stddraw.line(0,-1,10,-1)
    stddraw.setFontSize(50)
    stddraw.line(location['a'][0],location['a'][1],location['a'][2],location['a'][3])
    stddraw.line(location['b'][0],location['b'][1],location['b'][2],location['b'][3])
    stddraw.line(location['c'][0],location['c'][1],location['c'][2],location['c'][3])


    for d in dict.keys():
        stddraw.text(location[c][0],9,a+'-->'+c)
        n = len(dict[d])
        if n == 0:
            pass
        else:
            for i in range(1,n+2):
                print(i)
                stddraw.line(location[d][0]-i/n,8*(n+1-i)/(n+1),location[d][0]+i/n,8*(n-i+1)/(n+1))
                stddraw.text(location[d][0]-i/n-0.5,8*(n-i)/n,str(i))
            pass
    stddraw.show(300)

def move(location,dict,n, a, buffer, c):

    print('enter move program')
    stddraw.clear()

    print(dict)
    if(n == 1):

        print(a,"->",c)
        dict[c].insert(0,dict[a][0])

        del(dict[a][0])
        draw_move(dict,a,c,location)
        print(dict)

        return
    move(location,dict,n-1, a, c, buffer)
    move(location,dict,1, a, buffer, c)
    move(location,dict,n-1, buffer, a, c)


def main(n):

    dict={'a':[i for i in range(1,n+1)],'b':[],'c':[]}
    location = draw_setup(n)

    move(location,dict,n, "a", "b", "c")

main(5)