#跑得快 扑克牌
'''
规则说明：

1。 三方参与，其中2方为机器人，1方为用户
2。 扑克牌中抽取大小鬼，3个2，1个A出来。
3。 用户操作方法：
    1 - 发牌：
        1）每一轮最开始拿到发牌权
        2）每一轮中自己出牌后，其他所有用户都没有更大的牌可以跟。则拿到下一轮的发牌权。
    2 - 跟牌：每一轮中，从自己的牌中随机找到比上一张牌更大的牌发出
    3 - 放弃：每一轮中，自己的牌中没有比上一张牌更大的牌，则放弃
    4 - 赢牌：每一轮打完后，自己已经没有牌了
    5 - 报听：每一轮打完后，自己只剩一张牌了
4。每一轮随机生成打牌顺序
5。用户手动操作部分：选择打哪张牌。


'''

from stdpackage import stdrandom

def fapai(a,b,c):
    '''
    通过randomqueue.py 基于指定数据集生成3个随机牌列
    :param a: 用户a的牌列
    :param b: 用户b的牌列
    :param c: 用户c的牌列
    :return: 随机生成的3个用户的牌列 [a,b,c]
    '''


    return [a,b,c]

class Player:
    def __init__(self):
        self.cardlist = []
        self.next = None
        self.name = ''
        self.is_first = False
        
    def fapai(self):
        '''
        作为本小轮第一个出牌的人来发牌
        :return: 一张随机选择的牌
        '''
        randomindex = random(range(len(self.cardlist)))
        return self.cardlist.pop(randomindex)

    def chupai(self,last_card):
        '''
        根据牌面上本轮最后一张牌来判断自己要跟进还是PASS
        :param last_card:
        :return: 跟进的牌或者放弃的信号
        '''

        if has pai > last_card:
            pai = self.cardlist.pop(pai_index)
            return pai
        else:
            return 'pass'

    def is_win(self):
        '''
        判断本轮出完牌，是否自己胜利
        :return:
        '''

        return len(self.cardlist) == 0

    def callout(self):
        '''
        判断本轮出完牌，是否只剩1张牌
        :return: 是/否
        '''
        return len(self.cardlist) == 1

def first():
    '''

    :return: the starter
    '''
    player_list = []

    return random(player_list)

def main():

    #1 set players and order
    player_a = Player() #human
    player_b = Player()
    player_c = Player()
    player_c.next = player_a
    player_a.next = player_b
    player_b.next = player_c

    #2 fapai
    player_a.cardlist,player_b.cardlist,player_c.cardlist = fapai(player_a.cardlist,player_b.cardlist,player_c.cardlist)
    starter_player = first()
    print('start from player:'.format(starter_player.name))

    #3 play
    open_card_list = []

    while True:
        if open_card_list[-1][0] == player.name:
            player.fapai()
        player.chupai()
        if player.is_win(): print('player {0} win '.format(player.name));break
        if player.callout():print('player{0} call out'.format(player.name))








