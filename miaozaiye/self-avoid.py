#2D maxtrix, n*n. each position is a bool value, 'true' means never been here, 'false' means already been here.
#each step you have to chose one step forward: x: +1 or -1; y +1 or -1.
# if your chosen location is True, then you would remain alive in next turn, else you will lose.
# if your chosen location is True and is in the border, then you win.

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


class dog_inmatrix:
    def __init__(self,step,j,i,matrix):
        row_0 = random.randrange(1,j-1)
        line_0 = random.randrange(1,i-1)
        matrix[line_0][row_0]=False
        self.step = step
        self.location = (line_0,row_0)
        self.location_value = matrix[line_0][row_0]
        self.__trial = 0

        self.row_border = (0,j-1)
        # print('j is {0}'.format(j))
        # print('self.row_border is {0}'.format(self.row_border))
        self.line_border = (0,i -1)
        self.matrix = matrix
        self.valid_enviroment = []

    def check(self):
        print('now location is {0}'.format(self.location))
        # print('border is {0},{1}'.format(self.line_border,self.row_border))
        i = self.location[0]
        j = self.location[1]


        if self.location[0] in self.line_border or self.location[1] in self.row_border:
            print('win at the location{0}, with {1} steps'.format(self.location,self.__trial))
            return 'win'

        else:
            enviroment = 0
            self.valid_enviroment = []
            i_border_min = i - self.step if (i-self.step)>=0 else 0
            i_border_max = i+self.step if (i+self.step)<=self.line_border[1] else self.line_border[1]
            j_border_min = j - self.step if (j-self.step)>=0 else 0
            j_border_max = j+self.step if (j+self.step)<=self.row_border[1] else self.row_border[1]
            print(i_border_max,i_border_min)

            for i1 in[i_border_min,i_border_max]:

                for j1 in [j_border_min,j_border_max]:

                    enviroment += self.matrix[i1][j1]
                    # print('enviroment is {0}'.format(enviroment))
                    if self.matrix[i1][j1]:
                        a = (i1,j1)

                        self.valid_enviroment.append(a)
                # print(self.valid_enviroment)
            if enviroment == 0:
                print('fail at the location{0}, with {1} steps'.format(self.location,self.__trial))
                return 'fail'

            else:
                return False

    def move(self):
        self.__trial +=1
        length = len(self.valid_enviroment)
        location2 = self.valid_enviroment[random.randrange(length)]
        location_change =(location2[0] - self.location[0],location2[1] - self.location[1])
        self.location = location2
        self.matrix[location2[0]][location2[1]] = False

        print('move {0}x, {1}y, final location{2}'.format(location_change[0],location_change[1],self.location))


def main():
    row = int(input('please input row number:'))
    line = int(input('please input line number:'))
    step = int(input('please input step range:'))


    win_count = 0


    for i in range(500):
        matrix = creat2D(row,line,value = True)
        dog1 = dog_inmatrix(step,row,line,matrix)
        while True:
            if dog1.check():
                if dog1.check() == 'win':
                    win_count +=1
                break
            else:
                dog1.move()
    print ('total win {0} times'.format(win_count))

main()