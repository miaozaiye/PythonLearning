#!/usr/bin/env python
#coding:utf-8
import itchat

itchat.login()

itchat.send(u'hello','filehelper')

# 计算朋友圈男女比例
friends = itchat.get_friends(update=True)[0:]

male = female = other = 0

for i in friends[1:]:
	sex = i["Sex"]
	if sex == 1:
	 	male += 1
	elif sex == 2:
	 	female += 1
	else:
	 	other += 1

total = len(friends[1:])

print "male：%.2f%%" % (float(male) / total * 100)
print "female：%.2f%%" % (float(female) / total * 100)
print "other：%.2f%%" % (float(other) / total * 100)
