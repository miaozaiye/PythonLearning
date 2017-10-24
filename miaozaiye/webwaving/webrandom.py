#产生Web随机数据，类似 tiny.txt.
'''
数据格式：
第一行： 页面总数
从第二行开始：数组对：出发页面，到达页面

用户通过命令行输入：页面总数
最后生成：包含数据格式的txt文件

生成思路：

1： 遍历每个页面来生成
2： 当下页面，先随机生成 小于等于页面总数的整数，代表跳出的链接数（数组对的数量）
3： 遍历连接数，随机生成每个到达页面（不包括自身，可以重复）
4： 最后保存为 webrandom.txt

'''

import sys
from stdpackage import stdarray,stdio
import random

n = sys.argv[1]
fh = open('webrandom.txt','w')
fh.write(n+'\n')

n = int(n)

for page in range(n):
    targets = random.randint(0,n)
    for target in range(targets):
        link_target = random.randint(0,n)
        if link_target != page:
            fh.write(str(page)+' '+str(link_target)+' ')
        else: pass
    fh.write('\n')

fh.close()


