# 计算从某一个页面开始，最终可以到达目标页面的信息熵大小
# 信息熵越小（为负数），则信息值越高

'''
1。0
1 指定网页转化矩阵，类似 tiny.txt
2 指定其中目标页
3 计算跳转到目标页的比例

2。0
1 爬取网页，生成网页转化矩阵
2 其余同 1。0

'''
from stdpackage import stdarray

#定义webpage 类数据，可以手工输入每个网页上连接到的其他网址，以及对应的跳转概率
class webpage():
    print(' generate new webpage class object')
    def __init__(self,url):
        self.url = url
        self.link = []


    def getlink(self,list):
        self.link = list

def inputpage():
    print('enter inputpage')
    wb1 = webpage('https://proginn.com')
    wb1.getlink([['https://proginn.com/users',0.4],['https://proginn.com/help',0.2]])
    wb2 = webpage('https://proginn.com/users')
    wb2.getlink([['https://proginn.com',0.2],['https://proginn.com/help',0.1]])
    wb3 = webpage('https://proginn.com/help')
    wb3.getlink([['https://proginn.com',0.2],['https://proginn.com/users',0.2]])

    print (wb1.link,wb2.link,wb3.link)
    weblist = [wb1,wb2,wb3]
    print('return weblist')
    return weblist

# 通过3个网页的link数据，生成转化矩阵

def generate_transition_matrix(weblist):
    print('enter generate_transition_matrix()')

    transition_matrix = stdarray.create2D(3,3,0)
    wbnamelist = [weblist[i].url for i in range(len(weblist))]
    print(wbnamelist)
    for wb in weblist:
        i = wbnamelist.index(wb.url)
        for link in wb.link:
            j = wbnamelist.index(link[0])
            transition_matrix[i][j] = link[1]



    print('return transition_matrix:',transition_matrix)
    return transition_matrix

def count_entropy(weblist,start_page,targets,transiton_matrix,currentpossibility):
    '''
    entropy is the possibility to get into targets
    1, what's the possibility to get into target in start_page? count_down
    2, get_into non-target link with givin possibility,if givin possibility <0.01, return 0. else go step 1.

    :param targets:
    :param transiton_matrix:
    :return:
    '''
    if currentpossibility < 0.001:
        return 0

    star=wblist[start_page]
    for target in targets:
        start_page.link




    print('enter count_entropy()')
    entropy = 0
    print('return entropy')
    return entropy

def main():
    print('start main()')

    weblist = inputpage()
    transition_matrix = generate_transition_matrix(weblist)
    targets = input('please chose the index (1-3)target pages, use "," to split:')
    start_page = input('please chose start_page:')

    entropy = count_entropy(weblist,start_page,targets,transition_matrix)

    print('total entropy of current webpages are:',entropy)

main()