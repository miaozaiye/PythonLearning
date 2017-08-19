#扫雷游戏。 m*n 矩阵中，不规律分布有雷"*"， 每个没雷的单元格有数字显示，该单元格周围8个单元格的雷的总和。

'''
1） 生成含雷，和数字标识的矩阵
2）进入游戏模式：
   请用户输入坐标，以及行为（点开，标雷）
   动作如果是点开，返回坐标结果：是雷，则显示是雷，且已爆炸；不是雷，则返回数字结果。返回矩阵
   动作如果是标雷，则返回标雷后的矩阵
   动作如果是退出，则退出游戏

'''


import random

def creat2D(row,line,value = 0):
    assert isinstance(row,int),'row number must be int'
    assert isinstance(line,int),'line number must be int'

    array= []
    array_line=[]

    array = [None] * row
    for index in range(row):
        array[index] = [value]*line

    return array

class mine_matrix():
    def __init__(self,m,n):
        # print("------this is init-------")
        self.matrix = creat2D(m,n)
        self.m = int(m)
        self.n = int(n)
        self.mine_location = []
        self.mine_number = 0
        self.matrix_known = creat2D(m,n,value = 9)
        self.mark_record = []


    def create_new(self):
        # print('------this is create_new-------')
        # m,n = input('please input (line,row):').split(',')


        mine_number = int(self.m*self.n/6)
        self.mine_number = mine_number
        location = [(x,y) for y in range(self.n)for x in range(self.m)]
        location1 = location
        for i in range(mine_number):
            location_number = random.randrange(len(location1))
            mine_location=location1[location_number]

            self.matrix[mine_location[0]][mine_location[1]] = 'mine'
            location1.pop(location_number)
            self.mine_location.append(mine_location)

        for i in range(self.m):
            for j in range(self.n):
                i1_list = [i-1,i,i+1 ] if (i>0 and i <self.m-1) else ([i,i+1] if i == 0 else [i-1,i])
                j1_list = [j-1,j,j+1 ] if (j>0 and j <self.n-1) else ([j,j+1] if j == 0 else [j-1,j])

                if self.matrix[i][j]!='mine':
                    for i1 in i1_list:
                        for j1 in j1_list:
                            if i1 == i and j1 == j:
                                pass
                            else:

                                self.matrix[i][j] +=1 if self.matrix[i1][j1]=='mine' else 0


        return self.matrix

    def check(self,i,j):
        # print('-------this is check--------')
        if self.matrix[i][j] == 'mine':
            for line in self.matrix:
                print(line)
            print('you got bombed!')
            return False
        else:
            return True

    def mark(self,i,j):
        return 'm'

    def win(self):
        # print('--------this is win----------')
        if len(self.mark_record) == self.mine_number:

            self.mine_location.sort(key = lambda x:x[0])
            self.mark_record.sort(key = lambda x:x[0])
            if self.mine_location == self.mark_record:
                return True
            else:
                return False
        else:
            return False

    def print_matrix(self):
        # print('------this is print_matrix--------')
        for line in self.matrix:
            print(line)

    def print_known(self):
        # print('------this is print_known-------')
        for line in self.matrix_known:
            print(line)

    def operation(self,m,n,i,j,operation):
        # print('------operation-------')
        if operation == 'c':
            if not self.check(i,j):
                if not self.choice(m,n):

                    return False
                else:
                    return True
            else:
                self.matrixknown(i,j)
                return True

        if operation == 'm':
            self.matrix_known[i][j] = 'm'
            self.mark_record.append((i,j))
            return True


    def matrixknown(self,i,j):
        # print('-----matrixknown------')
        self.matrix_known[i][j] =self.matrix[i][j]
        # print('matrix_know[{0}][{1}] is {2}'.format(i,j,self.matrix_known[i][j]))
        # print('matrix[{0}][{1}] is {2}'.format(i,j,self.matrix[i][j]))




    def choice(self,m,n):
        # print('-----choice------')
        new_choice = input('would you want to start a new game(n) or to quit(q)?')

        if new_choice == 'n':
            print('start a new game with the same scale')
            self.__init__(m,n)
            self.create_new()
            return True



        else:
            return False

def new_choice(m,n):
    new_choice = input('would you want to start a new game(n) or to quit(q)?')

    if new_choice == 'n':
        print('start a new game with the same scale')
        mine1 = mine_matrix(m,n)


        return mine1

    else:
        return False

def main():
    m = int(input('please input m:'))
    n = int(input('please input n:'))

    mine1 = mine_matrix(m,n)
    mine1.create_new()


    while True:
        if mine1.win():
            print('you win!')
            for line in mine1.matrix:
                print (line)


            mine1 = new_choice(m,n)
            mine1.create_new()
            if not mine1:
                break

        mine1.print_known()

        choice= input('please input(i,j,[c]heck/[m]ark),or input "q" to quit:')

        if choice == 'q':
            print('you chose to quit the game')
            break
        else:
            i,j,operation = choice.split(',')
            i = int(i)
            j = int(j)
            op_result = mine1.operation(m,n,i,j,operation)
            # print('op_result is {0}'.format(op_result))
        if not op_result:
            break






main()




