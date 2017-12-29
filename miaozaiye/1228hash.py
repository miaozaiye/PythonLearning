#accept K-gram(a alphabetic string formed of "ACGT" with k charactors), and transfer to a hashed number

'''

1. accept k-gram
2. transfer each alphabet into an int in range of (0,3), with a pre-aligned correspondance.
3. transfer the int-list into an int.
4. un-hash: transfer the int into an int-list; transfer the list into alphabet list; tranfer into str.

'''
from stdpackage import stdarray

class myhash:
    def __init__(self,alphabetgroup):


        self.string = ''
        self.alphabetgroup = alphabetgroup
        self.transition_matrix = {}
        self.utransition_matrix = {}
        for i in range(len(self.alphabetgroup)):
            self.transition_matrix[self.alphabetgroup[i]] = str(i)
            self.utransition_matrix[str(i)] = self.alphabetgroup[i]
        print('hash matrix is:\n',self.transition_matrix)
        print('un-hash matrix is:\n',self.utransition_matrix)
        self.int = 0



    def _transfer(self,choice,obj):
        '''
        1.check if obj is int or alphabet
        2. if it's int, do un-hash
        3. if it's alphabet, do hash
        4. return result

        :param alphabetgroup:
        :return:
        '''

        if choice == 'h':
            transffered_obj = self.transition_matrix[obj]
        if choice == 'u':
            transffered_obj = self.utransition_matrix[obj]



        return transffered_obj



    def setstr(self,string):
        self.string = string

    def setint(self,intiger):

        self.int = intiger

    def transferstr(self,choice):

        if choice == 'h':

            k = len(self.string)
            string = self.string

        if choice =='u':
            k = len(str(self.int))
            string = str(self.int)


        list_new = stdarray.create1D(k,0)
        for i in range(len(string)):

            list_new[i] = str(self._transfer(choice, string[i]))

        tmp = ''
        print(list_new,type(list_new))
        for item in list_new:
            print('item is:',item)
            tmp +=item
        print('tmp is:',tmp)

        return tmp

    def hash(self):
        '''
        1.create a list with k element
        2.call transfer function to transfer


        :return: hashed number
        '''
        result = self.transferstr('h')

        return result

    def un_hash(self):


        unhash_result = self.transferstr('u')

        return unhash_result

def main():
    gene = myhash('GACDT')
    gene.setstr('GACT')
    hashresult = gene.hash()
    print('this is the hash result,',hashresult)
    gene.setint(hashresult)

    print('this is the unhash result,',gene.un_hash())


main()