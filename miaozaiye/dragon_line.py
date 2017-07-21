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

print (dragonline.turn_flow(5))
