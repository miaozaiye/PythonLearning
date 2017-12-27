#爬取目标网页信息，生成 Webpage类型数据，以及webpage list。

'''
1. import webpage class
2. parse page1, set page1 in webpage class, add into weblist  if it's not in list before.
3. go into link in body part, repeat step 2 -3.
4. return final weblist


'''


# from miaozaiye.webwaving.entropy import webpage
import requests
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen

#定义webpage 类数据，可以手工输入每个网页上连接到的其他网址，以及对应的跳转概率
class webpage():
    print(' generate new webpage class object')
    def __init__(self,url):
        self.url = url
        self.link = []


def parse_link(url_0):



    wb_data=requests.get(url_0,'utf-8')
    soup=BeautifulSoup(wb_data.text,'lxml')

    url_list = [['https://proginn.com',0.2]]
    print('return url_list')
    return url_list

def generate_weblist(url_0,weblist):

    #1 check if url is in database, if not:
    #2      parse all links in link0, combine them into one group. put into database
    #3      dive into link_i, repeat step 1 - 3
    #4 if yes, pass this url.
    #
    web = webpage(url_0)
    web.link = parse_link(url_0)
    print('web is {0}, web.link is {1}'.format(web,web.link))
    if web in weblist:
        print('web in list')
        return weblist
    else:
        weblist.append(web)
        print('weblist is {0}'.format(weblist))
        for link in web.link:
            print('link is:',link)
            generate_weblist(link[0],weblist)

    return weblist

url_0 = 'https://proginn.com'
generate_weblist(url_0,[])