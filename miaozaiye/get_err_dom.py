#explanation of err that user inputs
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
import xml.dom.minidom

file = '/Users/Jane/Desktop/Python 全栈学习/python3 learning/lesson7/errorlist'
filename = '/Users/Jane/Desktop/Python 全栈学习/python3 learning/lesson7/err_object_domlist.txt'

GZIP_MAGIC = 'abc'

class err_object():
    '''
    属性：
    key: lowercase str
    name: Title str
    explanation: 中文解释的句子
    example: 实例，包括命令行，出错提示

    方法：
    导出到二进制文件
    从二进制文件导入


    '''

    def __init__(self,key,name,explanation,example):
        self.key = key
        self.name = name
        self.explanation = explanation
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

                errlist[eng.lower()]=err_object(eng.lower(),eng,chi,example_content)


                # print('eng is{0}'.format(eng))
                #
                # print('err name is {0}'.format(one_err.name))
                example_content = ''

    for key in errlist:
        print('errlist[{0}]: {1}\n{2}'.format(key,errlist[key].key,errlist[key].name))
    export_xml_dom(errlist,filename)
    return errlist




def export_xml_dom(errlist, filename, compress=False):

    '''

    xml 的格式：

    <?xml> version ='1.0' encoding = 'UTF-8'
    <root>
    <element attribute1 = value1 attribute2 = value2 ...>
    <sub-element>text</sub-element>
    </element>

    <element>
    ......
    </element>
    </root>


    导入导出的时候，都是基于这个格式来操作
    '''

    fh = None
    dom = xml.dom.minidom.getDOMImplementation()
    tree = dom.createDocument(None,'err_object',None)
    root = tree.documentElement

    for err_object in errlist:
        print('err_object is {0}:{1}'.format(err_object,errlist[err_object].name))
        element = tree.createElement('err_object')
        for attribute,value in (
                ('key',errlist[err_object].key),
                ('name',errlist[err_object].name),
                ('explanation',errlist[err_object].explanation),
                ('example',errlist[err_object].example)

        ):
            element.setAttribute(attribute,value)
            print('element name is {0}'.format(errlist[err_object].name))
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
    errlist = {}


    def get_text(node_list):
        text = []
        for node in node_list:
            if node.nodeType == node.TEXT_NODE:
                text.append(node.data)
        return "".join(text).strip()

    try:
        dom = xml.dom.minidom.parse(filename)


    except (EnvironmentError,
            xml.parsers.expat.ExpatError) as err:
        print("{0}: import error: {1}".format(
              os.path.basename(sys.argv[0]), err))
        return False


    for element in dom.getElementsByTagName("err_object"):


        try:
            data = {}
            for attribute in ('key', 'name', 'explanation', 'example'):
                data[attribute] = element.getAttribute(attribute)

            err_object1 = err_object(**data)
            errlist[err_object1.key] = err_object1

        except (ValueError, LookupError) as err:
            print("{0}: import error: {1}".format(
                  os.path.basename(sys.argv[0]), err))
            return False
    return errlist


def print_exp(err,filename):
    #show the err explanation and examples
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
    err_object_list = import_xml_dom(filename)



    assert err.lower() in err_object_list,'{0} not in errlist'.format(err) # robust in lower and upper case
    err_object = err_object_list[err.lower()] # use the standard key to get right content

    print(
        '{0} is {1}\n ******以下是实例******\n{2}'.format(err_object.name, err_object.explanation,
                                                  err_object.example)
    )





def main():
    '''

    >>>get_err.py -h
    Usage: get_err.py [options]

    Options:
    -h, --help         show this help message and exit
    -e ERR, --err=ERR  get the explanation of the err

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
            help=("get the explanation of the err"))

    opts, args = parser.parse_args()

    err = opts.err


    print_exp(err,filename)


main()
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
