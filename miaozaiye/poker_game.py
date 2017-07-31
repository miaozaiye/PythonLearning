#拖拉机：一副牌，洗乱之后分为2堆，然后按顺序发牌。出现和前面一样的牌，则可以把两个牌之间所有牌都收归自己所有，放到最尾部。
#当一方手上没有牌时为输，或者指定回合后，牌多的人取胜。

'''
1 - 生成所有的牌的列表：花色，数字
2 - 洗牌打乱顺序
3 - 按顺序发牌到两堆
4 - 随机选择先发牌一方
5 - 按顺序每方发一张牌
6 - 如果发的牌在前面有同样数字的牌，则两张牌及中间的所有都归于发牌方
7 - 如果有一方没有牌了，则判为输
8 - 如果到了第100回合，则牌多的人赢

'''
import random

#1

def generate_poker():
    SUITS = ['Clubs','Diamonds','Hearts','Spades']
    RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append([suit,rank])


    return deck
#2

def shuffle_poker(deck):
    random.shuffle(deck)
    return deck
#3

def deliver_poker(deck):
    player_1 = deck[0::2]
    player_2 = deck[1::2]
    print(deck)
    print(player_1,'\n',player_2)
    return player_1,player_2

# 5-8
def play_poker(player_1,player_2):
    deck_new = []
    n = 0
    print('n is {0}'.format(n))
    while True:
        for i in ['1','2']:
            if len('player_{0}'.format(i)) == 0:
                print ('player_{0} failed'.format(i))
                break
        if n == 100:
            print('n is {0}'.format(n))
            len1 = len(player_1)
            len2 = len(player_2)
            result = 'player_1 win' if len1>=len2 else 'player_2 win'
            print (result)
            break

        if n == 0:
            print("player_1's turn : {0}".format(player_1[0]))
            deck_new.append(player_1[0])
            player_1.pop(0)
            print("Now deck is {0}".format(deck_new))

            print("player_2's turn : {0}".format(player_2[0]))
            if player_2[0][1] == deck_new[0][1]:
                cut = deck_new[0]
                cut.append(player_2[0])
                player_2.pop(0)
                player_2.append(cut)
                print("player_2 get cut:{0}".format(cut))
            else:

                deck_new.append(player_2[0])
                player_2.pop(0)
                print("Now deck is {0}".format(deck_new))

        for i in range(len(deck_new)):
            print('player_1 is:{0}'.format(player_1))
            print("player_1's turn : {0}".format(player_1[0]))
            if player_1[0][1] == deck_new[i][1]:
                cut = deck_new[i:]
                cut.append(player_1[0])
                print('cut is {0}'.format(cut))
                player_1.pop(0)
                player_1 +=cut
                print("player_1 get cut:{0}".format(cut))
            else:

                deck_new.append(player_1[0])
                player_1.pop(0)

                break

        for i in range(len(deck_new)):
            print("player_2's turn : {0}".format(player_2[1]))
            if player_2[0][1] == deck_new[i][1]:
                cut = deck_new[i:]
                cut.append(player_2[0])
                player_2.pop(0)
                player_2+=cut
                print("player_2 get cut:{0}".format(cut))
            else:

                deck_new.append(player_2[0])
                player_2.pop(0)

                break
        print('n is {0}'.format(n))
        n+=1


deck = generate_poker()
deck = shuffle_poker(deck)

player_1,player_2 = deliver_poker(deck)
play_poker(player_1,player_2)