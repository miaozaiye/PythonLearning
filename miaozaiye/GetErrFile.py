'''
类是一个列表，每个单位是一个错误子类。
子类包括：key,name,中文

类可以存入新的err，但是要求格式都满足要求。
不可以重复存入同样的err, 如果存入则会提示错误，且中断程序。
类可以删除指定key的err,删除后不可正常访问，除非恢复正常状态。

>>>err1 = ErrObj('abcd','Abcd','第一个')
>>>err1.chiname
第一个
>>>file = ErrFile(filename)
>>>file.errappend('abcd','Abcd','第一个')
now point at 0
[('abcd', 0)]
>>>file.errappend('abdd','Abdd','第二个')
now point at 22
[('abcd', 0), ('abdd', 22)]
>>>file.errappend('dfav','Dfav','第四个')
now point at 44
[('abcd', 0), ('abdd', 22), ('dfav', 44)]

'''

import os

filename = os.getcwd()+'/errfile.txt'
OKAY = 'y%'
DELE = 'd%'


class ErrObj:

    def __init__(self,key,name,chiname):
        assert len(key)<20,"key's length is out of range"
        assert len(name)<20,"name's length is out of range"
        assert len(chiname)<20,"chiname's length is out of range"

        self.key = key
        self.name = name
        self.chiname = chiname

class ErrFile:
    def __init__(self,filename,autoflush = True):
        '''
        创建类，打开文件准备之后的类操作

        '''
        mode = 'w+' if not os.path.exists(filename) else 'r+'
        self.__fh = open(filename,mode)
        self.__searchlist = []
        self.__delhistory = []
        self.autoflush = autoflush

    def errappend(self,key,name,chiname):
        '''
        增加内容到类最末尾
        并储存对应的Key，以及位置

        '''

        print('now point at {0}'.format(self.__fh.tell()))
        self.__fh.seek(0,2)
        errkey,location = key,self.__fh.tell()
        self.__searchlist.append((errkey,location))
        print(self.__searchlist)

        errobj =OKAY+key+'/'+name+'/'+chiname+'\n'
        self.__fh.write(errobj)
        if self.autoflush:
            self.__fh.flush()

    def errdel(self,key_in_search):
        '''
        根据key 来删除对应位置的内容

        找到key 对应的内容，修改OKEY 为 DELE.
        之后每次读取，发现状态符号为DELE则机器会返回已删除的结果。
        >>>file.get_err('abcd')
        abcd/Abcd/第一个
        >>>file.errdel('abcd')
        status is y
        status changed to deleted
        mission accmplished
        >>>file.errdel('abcd')
        no such key

        '''
        a = 0
        for key,location in self.__searchlist:
            if key == key_in_search :
                self.__fh.seek(location)
                status = self.__fh.read(1)
                print ('status is {0}'.format(status))
                a = 1

                if status == DELE:
                    pass
                else:
                    self.__fh.seek(location)
                    self.__fh.write(DELE)
                    self.__delhistory.append((key,location))
                    print('status changed to deleted')
            else:
                pass

        reply = 'mission accomplished' if a==1 else 'no such key'
        print (reply)
        if self.autoflush:
            self.__fh.flush()

    def undel(self,key_in_search):
        '''
        如果输入的Key在 searchlist 里面，且已经被删除，则恢复,同时从删除历史里面移除删除记录；
        未被删除，则提示未被删除。
        如果输入的Key不在Search list里面，则提示没有这个Key

        >>>file.errdel('abcd')
        mission accomplished
        >>>file.undel('abcd')
        abcd is undeleted:abcd/Abcd/第一个
        >>>file.undel('abaa')  #'abaa'并不存在
        abdd is not in errlist
        >>>file.undel('dfav')
        dfav is not deleted:dfav/Dfav/第四个
        '''
        a = 0
        for key,location in self.__searchlist:
            if key == key_in_search:
                a = 1
                self.__fh.seek(location)
                if self.__fh.read(2)!= DELE:
                    reply1 = '{0} is not deleted:{1}'.format(key,self.__fh.read(16))
                else:
                    self.__fh.seek(location)
                    self.__fh.write(OKAY)
                    self.__delhistory.remove((key,location))
                    reply1 = '{0} is undeleted:{1}'.format(key,self.__fh.read(16))
        reply = '{0} is not in errlist'.format(key_in_search) if a == 0 else reply1

        return reply

    def get_err(self,input_key):

        '''
        根据input_key 来找到对应位置的内容,然后返回

        >>>file.get_err('abcd')
        abcd/Abcd/第一个
        >>>file.errdel('abcd')
        mission accmplished
        >>>file.get_err('abcd')
        sorry, abcd is not in errlist

        '''

        a = 0

        for key,location in self.__searchlist:
            if key == input_key.lower():
                self.__fh.seek(location)
                if self.__fh.read(2)!= DELE:
                    a = 1
                    self.__fh.seek(location+2)
                    return self.__fh.read(14)

        if a == 0:
            return 'sorry, {0} is not in errlist'.format(input_key)

    @property
    def del_history(self):

        return [key for key,location in self.__delhistory]



    def close(self):

        self.__fh.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()