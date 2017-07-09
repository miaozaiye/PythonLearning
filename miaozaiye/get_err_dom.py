#explaination of err that user inputs
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
import xml.dom.minidom

file = '/Users/Jane/Desktop/Python 全栈学习/python3 learning/lesson7/errorlist'
filename = '/Users/Jane/Desktop/Python 全栈学习/python3 learning/lesson7/err_object_domlist.txt'

GZIP_MAGIC = 'abc'

class err_object():
    '''
    属性：
    key: lowercase str
    name: Title str
    explaination: 中文解释的句子
    example: 实例，包括命令行，出错提示

    方法：
    导出到二进制文件
    从二进制文件导入


    '''

    def __init__(self,key,name,explaination,example):
        self.key = key
        self.name = name
        self.explaination = explaination
        self.example = example


def get_filelist(filename):
    '''
    读取原始文件数据，清理数据成想要的格式，在文件运行时转换成对象字典

    '''
    fh = open(file,'r')
    example_content = ''
    errlist = {}
    a = 0
    chi = ''

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
                example_content +=line


            else:
                a = 0
                one_err.key = eng.lower()
                one_err.name = eng
                one_err.explaination = chi
                one_err.example = example_content

                errlist[one_err.key]=[one_err.key,one_err.name,one_err.explaination,one_err.example]

                # print('eng is{0}'.format(eng))
                #
                # print('err name is {0}'.format(one_err.name))
                example_content = ''

    export_xml_dom(errlist,filename)
    return errlist




def export_xml_dom(errlist, filename, compress=False):
    fh = None
    dom = xml.dom.minidom.getDOMImplementation()
    tree = dom.createDocument(None,'err_object',None)
    root = tree.documentElement
    for err_object in errlist:
        element = tree.createElement('err_object')
        for attribute,value in (
                ('key',err_object[0]),
                ('name',err_object[1]),
                ('explaination',err_object[2]),
                ('example',err_object[3])

        ):
            element.setAttribute(attribute,value)
        root.appendChild(element)

    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        tree.writexml(fh, encoding="UTF-8")
        return True
    except EnvironmentError as err:
        print("{0}: export error: {1}".format(
              os.path.basename(sys.argv[0]), err))
        return False
    finally:
        if fh is not None:
            fh.close()


def import_xml_dom(filename):
    fh = None
    try:
        fh = open(filename, "rb")
        magic = fh.read(len(GZIP_MAGIC))
        if magic == GZIP_MAGIC:
            fh.close()
            fh = gzip.open(filename, "rb")
        else:
            fh.seek(0)

        errlist = pickle.load(fh)



        return errlist
    except (EnvironmentError, pickle.UnpicklingError) as err:
        print("{0}: import error: {1}".format(
              os.path.basename(sys.argv[0]), err))
        return False
    finally:
        if fh is not None:
            fh.close()
    return errlist




def print_exp(err,filename):
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
    #如果目标二进制文件不存在，则读取原始数据，数据整理并存到目标文件内。
    if not os.path.exists(filename) :
        errlist = get_filelist(filename)

    #此时 err_object_list.txt 文件应该已经存在，如果还不存在，一定发生了不可知意外，需要终止
    assert 'err_object_list.txt','file not exist'

    #获取文件数据
    err_object_list = import_pickle(filename)


    assert err.lower() in err_object_list,'{0} not in errlist'.format(err) # robust in lower and upper case
    err_object = err_object_list[err.lower()] # use the standard key to get right content

    print(
        '{0} is {1}******以下是实例******\n{2}'.format(err_object[1],err_object[2],
                                                  err_object[3])
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


    print_exp(err,filename)


main()
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
