# this file is to show the explaination of err that user inputs
'''

 This programme is to show the chinese name of the error, it's function and it's example.
 It's robust, unsensitive about lower or upper case. 'syntaxError', 'SYNtaxerrOR' all equal to 'SyntaxError'

>>> get_err.py zerodivisionerror

ZeroDivisionError：除数为0
>>> v = 1/0
ZeroDivisionError: int division or modulo by zero

'''

import sys,os
import optparse
import getopt
import gzip
import pickle

file = '/Users/Jane/Desktop/Python 全栈学习/python3 learning/lesson7/errorlist'

GZIP_MAGIC = 'abc'

class err_object():
    '''
    属性：
    key: lowercase str
    name: Title str
    explaination: 中文解释的句子
    example: 实例，包括命令行，出错提示

    方法：
    1：是否允许直接修改值？不允许。属性都只能是内在属性，可读不可写，通过函数返回值
    2：属性的数值判断和反馈,考虑装饰器

    '''

    def __init__(self,key,name,explaination,example):
        self._key = key
        self._name = name
        self._explaination = explaination
        self._example = example

    def key(self):
        return self._key

    def name(self):
        return self._name

    def explaination(self):
        return self._explaination

    def example(self):
        return self._example


def get_filelist(path):
    '''
    读取原始文件数据，清理数据成想要的格式，在文件运行时转换成对象字典

    '''
    fh = open(file,'r')
    content = ''
    err = {}
    a = 0

    for line in fh:
        one_err = err_object
        if a == 0:
            try:
                if int(line.split('、')[0]):
                    a = 1
                    index,line2 = line.split('、')

                    eng,chi = line2.split('：')[0] or 'not exist',line2.split('：')[1] or 'not exist'

            except Exception:
                pass
        elif a == 1:
            if line != '\n':
                content +=line


            else:
                a = 0
                err[eng.lower()]=[one_err.name(),one_err.explaination(),one_err.example()]
                content = ''


    export_pickle(err)
    #存到对象列表，然后pickle dump to file
    return err

def export_pickle(err):
    '''
    将err用Pickele 导出保存为二进制文件，文件名 err_object.txt
    :param err:
    :return:
    '''




def import_pickle(file):
    fh = None
    err1 = []
    try:
        fh = open(file, "rb")
        magic = fh.read(len(GZIP_MAGIC))
        if magic == GZIP_MAGIC:
            fh.close()
            fh = gzip.open(file, "rb")
        else:
            fh.seek(0)
        print ('pickle.load(fh) is {0}'.format(pickle.load(fh)))
        err1.append(pickle.load(fh))

        return True
    except (EnvironmentError, pickle.UnpicklingError) as err:
        print("{0}: import error: {1}".format(
              os.path.basename(sys.argv[0]), err))
        return False
    finally:
        if fh is not None:
            fh.close()

errlist = err_list(file)

def print_exp(err,errlist):
    #show the err explaination and examples
    '''
    >>> get_err.py synta
    AssertionError:not in errlist

    >>> get_err.py nAMeerror
    NameError is 尝试访问一个未申明的变量
    ******以下是实例******
    >>> v
    NameError: name 'v' is not defined



    '''

    if 'err_object.txt' not exist:
        create file

    assert file exist,'file not exist'

    errdata = import_pickle(file)

    # print('err is {0}'.format(err))


    assert err.lower() in errdata.key,'{0} not in errlist'.format(err) # robust in lower and upper case
    err_object = errdata[err.lower()] # use the standard key to get right content
    print(
        '{0} is {1}******以下是实例******\n{2}'.format(err_object.name(),err_object.example(),
                                                  err_object.example())
    )





def main():
    '''

    >>>get_err.py -h
    Usage: get_err.py [options]

    Options:
    -h, --help         show this help message and exit
    -e ERR, --err=ERR  get the explaination of the err

    >>>get_err.py -e syntaxerror
    SyntaxError is 语法错误
    ******以下是实例******
    >>> int int
    SyntaxError: invalid syntax (<pyshell#14>, line 1)


    >>>

    '''
    parser = optparse.OptionParser("""\
usage: %prog [options] infile outfile

tell you what the err mean and its example. not sensitive on lower/upper case.""")

    parser.add_option("-e", "--err", dest="err",
            help=("get the explaination of the err"))

    opts, args = parser.parse_args()

    err = opts.err


    print_exp(err,errlist)


main()
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

