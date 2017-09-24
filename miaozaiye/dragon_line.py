# draw dragon line base on requested times
'''
altorithm:

1st move: [F]oward
2nd move: [L]eft turn
3rd move: [F]oward

the n'nd wrap, will create 2^(n-1)'s turnning point, and they follow the order(LRLRLRLR),
in the location(1,3,5,..-3,-1), while turning direction at location x would be the opposite of location -x.

total turning point would be:

1 + 2^(2-1)+2^(3-1)+...+2^(n-1)

it's n'nd wrap:

location i's turning should be:

l_new[i] = 'L' if i%2 == 0 else 'R'
l_n[i] = l_new[i/2] if i%2 == 0 else l_(n-1)[int(i/2)]


'''

from stdpackage import stddraw
import math

class DragonLine:
    def __init__(self):

        self.__turnflow = []


    def turn_flow(self,wrap):

        flow_origin = self.turn_flow(wrap-1) if wrap>2 else ['L']
        flow_new = ['L' if i%2 ==0 else 'R' for i in range(2**(wrap-1))]
        self.__turnflow = [i for i in range(2**wrap-1)]
        _range = 2**wrap-1
        self.__turnflow = [flow_new[int(i/2)] if i%2 == 0 else flow_origin[int(i/2)] for i in range(_range)]


        return self.__turnflow


dragonline = DragonLine()

def draw_line(dragonline,turn):
    stddraw.setXscale(-5,5)
    stddraw.setYscale(-5,5)
    stddraw.setFontSize(20)


    theta = 0
    x_list = [0,1]
    y_list = [0,0]
    stddraw.line(x_list[0],y_list[0],x_list[1],y_list[1])
    x = 1
    y = 0
    List = dragonline.turn_flow(turn)
    Turn = [(1,0),(0,1),(-1,0),(0,-1)]
    for index in range(2*(turn-1)+1):
        det_theta = 1 if List[index] =='L' else -1
        theta =(theta + det_theta)%4

        det_x = Turn[theta][0]
        det_y = Turn[theta][1]
        x = x+det_x
        y = y+det_y

        x_list.append(round(x))
        y_list.append(round(y))

        stddraw.setPenColor(stddraw.BLACK)
        stddraw.line(x_list[index],y_list[index],x_list[index+1],y_list[index+1])
        stddraw.setPenColor(stddraw.RED)
        # stddraw.text(x_list[index],y_list[index],'({0},{1}) to ({2},{3})'.format(x_list[index],y_list[index],x_list[index+1],y_list[index+1]))
        # stddraw.text(x_list[index],y_list[index],str(index))
        stddraw.show(50)


draw_line(dragonline,30)
