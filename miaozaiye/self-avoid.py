#2D maxtrix, n*n. each position is a bool value, 'true' means never been here, 'false' means already been here.
#each step you have to chose one step forward: x: +1 or -1; y +1 or -1.
# if your chosen location is True, then you would remain alive in next turn, else you will lose.
# if your chosen location is True and is in the border, then you win.

import random


def creat2D(row,line,value = 0):
    assert isinstance(row,int),'row number must be int'
    assert isinstance(line,int),'line number must be int'
    print()
    array= []
    array_line=[]

    array = [None] * row
    for index in range(row):
        array[index] = [value]*line

    return array


class dog_inmatrix:
    def __init__(self,step,i,j):
        self.step = step
        self.location = (i,j)
        self.location_value = matrix[i][j]
        self.__trial = 0
        self.valid_enviroment =[]

    def check(self):


        if self.location[0] in line_border or self.location[1] in row_border:
            print('win at the location{0}, with {1} steps'.format(self.location,self.__trial))
            return False

        else:
            enviroment = 0

            for i1 in(i+1,i-1):
                for j1 in (j+1,j-1):
                    enviroment += matrix[i1][j1]
                    if matrix[i1][j1]:
                        self.valid_enviroment.append((i1,j1))
            if enviroment == 0:
                print('fail at the location{0}, with {1} steps'.format(self.location,self.__trial))
                return False

            else:
                return True

    def move(self):
        self.__trial +=1
        length = len(self.valid_enviroment)
        self.location = self.valid_enviroment[random.randrange(length)]



def main():
    row = int(input('please input row number:'))
    line = int(input('please input line number:'))

    matrix = creat2D(row,line,value = True)
    row_0 = random.randrange(row)
    line_0 = random.randrange(line)
    start_point = matrix[row_0][line_0]

    row_border = row-1
    line_border = line -1

    dog1 = dog_inmatrix(1,row_0,line_0)
    while True:
        dog1.check()
        dog1.move()
