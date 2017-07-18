'''
类是一个列表，每个单位是一个错误子类。
子类包括：key,name,中文

类可以存入新的err，但是要求格式都满足要求。
不可以重复存入同样的err, 如果存入则会提示错误，且中断程序。
类可以删除指定key的err,删除后不可正常访问，除非恢复正常状态。

'''

import os

filename = os.getcwd()+'/errfile.txt'
OKAY = ' y%'
DELE = ' d%'


class ErrObj:

    def __init__(self,key,name,chiname):
        assert len(key)<20,"key's length is out of range"
        assert len(name)<20,"name's length is out of range"
        assert len(chiname)<20,"chiname's length is out of range"
        self.key = key
        self.name = name
        self.chiname = chiname

class ErrFile:
    def __init__(self,filename):

        mode = 'w' if not os.path.exists(filename) else 'r'
        self._fh = open(filename,mode)

    def errappend(self,key,name,chiname):
        print('1 now point at {0}'.format(self._fh.tell()))
        self._fh.seek(0,2)

        errobj =OKAY+key+'/'+name+'/'+chiname
        self._fh.write(errobj)


err1 = ErrObj('abcd','Abcd','第一个')

print(err1.chiname)

file = ErrFile(filename)
file.errappend('abcd','Abcd','第一个')
file.errappend('abdd','Abdd','第二个')
file.errappend('abdd','Abdd','第三个')