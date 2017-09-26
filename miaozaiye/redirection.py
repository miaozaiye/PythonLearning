#根据需求将标准输出输出到对应的位置（文档，控制台，等）
#原理是全部存到缓存中，根据要求输出到控制台或者文档

import sys

class __redirection__:

    def __init__(self):
        self.buff = ''
        self.__console__ = sys.stdout

    def write(self,output_stream):
        self.buff +=output_stream

    def to_console(self):
        sys.stdout = self.__console__
        print (self.buff)

    def to_file(self,file_path):
        f= open(file_path,'w')
        sys.stdout = f
        print (self.buff)
        f.close()

    def flush(self):
        self.buff = ''

    def reset(self):
        sys.stdout = self.__console__


r_obj = __redirection__()
sys.stdout = r_obj

print('hello')
print('there')
r_obj.to_console()
r_obj.to_file('redirection.log')
r_obj.flush()
r_obj.reset()