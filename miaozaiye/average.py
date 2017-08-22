import sys

'''
标准输入输出流：

func att args > data.txt   # 程序直接输出到文件
func < data.txt #程序从文件读取信息


python 的输入输出函数
http://blog.csdn.net/pipisorry/article/details/24143801
sys.stdin.read(), sys.stdin.readline(),sys.stdout

'''


content = sys.stdin.read()

for line in content:
    print('this is line:{0}'.format(line))