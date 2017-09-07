#目标：
# 爬取程序员客栈的好评榜，总结各个方向好评最多的开发者，并将好评根据"态度好"，"专业"，"效率高" 进行分类，找到该开发者的最大优势
# 找到企业方愿意打5星，并愿意继续合作的关键因素
'''

1： 爬取页面信息，按照以下格式保存到文档：
    评价的内容，企业方，开发者，方向，技能（如果没有则填None）

2： 对评价的内容进行清洗整理，语义分析，找到企业方愿意打5星，并愿意继续合作的关键因素

3： 对开发者在三个方面的得分进行计算，以及排名，给出推荐

'''

import pymongo
from bs4 import BeautifulSoup
import requests
import time
import sys
from QcloudApi.qcloudapi import QcloudApi
from mongoengine import *

# client = pymongo.MongoClient('localhost',27017)
# proginn_COMMENT = client['proginn_COMMENT']
# sslk3 = proginn_news['sslk3']
# sslklinks2 = proginn_news['sslklinks2']
# linkexists3 = proginn_news['linkexists3']
# zhihu_cxykz3 = proginn_news['zhihu_cxykz3']
# linkexists_ZH1 = proginn_news['linkexists_ZH1']
# weibo = proginn_news['weibo']
# linkexists_weibo = proginn_news['linkexists_weibo']
#
# v2ex=proginn_news['v2ex']
# linkexists_v2ex = proginn_news['linkexists_v2ex']


url_0 = 'https://www.proginn.com/user/comment?p='

def get_goodcomments(url_0):


    Comments = [ ]
    good_employee = {}
    tmp = sys.stdout
    f = open('parse_proginn.log','w')
    sys.stdout = f

    for page in range(1,31):
        url = url_0+str(page)
        print(url)
        time.sleep(1)
        wb_data=requests.get(url,'utf-8')
        soup=BeautifulSoup(wb_data.text,'lxml')


        comments = soup.select('div.comment')
        employees = soup.select('.name')

        print('this is page{0}'.format(page)) 

        for comment,employee in zip(comments,employees):
            # print(comment)
            for line in comment:
                comment1 = line.lstrip().rstrip()
            print(comment1)

            for line in employee:
                employee1 = line

            if employee1 in good_employee.keys():
                good_employee[employee1].append(comment1)
            else:
                good_employee[employee1]=[comment1]
            Comments.append(comment1)



    sys.stdout=tmp
    f1 = open('proginn_comments.txt','w',encoding='utf-8')
    print('over, pls. check log in <parse_proginn.log>')
    for item in Comments:
       f1.write(item+'\n')
    f1.close()

    # f2 = open('proginn_good_employee.txt','w',encoding='utf-8')
    # for item in good_employee:
    #
    #     f2.write(good_employee+'\n')
    # f2.close()

    print(Comments)
    print(good_employee)




get_goodcomments(url_0)
