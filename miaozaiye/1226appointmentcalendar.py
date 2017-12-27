#创造一个日历年的预约日程安排。
'''

每个预约安排包括：
1。 开始时间
2。 结束时间
3。 地点
4。 内容
5。 预约对象

日程可以检查：
1。 指定时间有没有预约安排
2。 和指定人什么时候有预约安排
3。 创建预约的时候，判断时间是否有冲突

客户端测试：
1。创造一个预约
2。创造一个时间上有冲突的预约
3。询问某个时间段是否有预约
4。询问和某个人是否有预约

'''

from datetime import datetime
import time
import sys

class appointment:
    def __init__(self,start,end,who,location = '',content = ''):
        self.start = start
        self.end = end
        self.who = who
        self.location = location
        self.content = content
        start_datetime = datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M')
        end_datetime = datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M')
        self.str = 'you have appointment with {0} from {1} to {2} at location {3},topic is {4}'.format(who,start_datetime,end_datetime,location,content)


class calendar:
    def __init__(self):
        self.calendar = []

        pass

    def timecomflict(self,start,end):
        count = 0
        for appointment in self.calendar:

            if start >= appointment.start and end <appointment.end:
                print(appointment.str)

                count +=1
                return True

        if count == 0:
            return False

    def add_appointment(self,appointment):
        '''
        往Calendar添加一个预约。
        判断如果有时间冲突，则反馈时间冲突。
        如果没有时间冲突，则添加成功,并返回整体Calendar
        :param appointment:
        :return:
        '''

        if self.timecomflict(appointment.start,appointment.end):
            print ('timecomflict')
            return self.calendar

        else:
            self.calendar.append(appointment)
            print('sucess! add to calendar')

        return self.calendar

    def checktime(self,time):
        if self.timecomflict(time,time+1):

            print ('you have appointment above')

        else:
            print ('you have no appointment at {0}'.format(datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%D')))

    def checkname(self,name):
        count = 0
        list = []
        for appointment in self.calendar:
            if name == appointment.who:
                list.append(appointment)
                print (appointment.str)
                count +=1

        print('total {0} appointment with {1}'.format(count,name))
        return list




def main():
    startinput = input('please input start time:YYYY-MM-DD HH：MM:SS')
    endinput = input('please input end time:YYYY-MM-DD HH：MM:SS')


    start = time.mktime(datetime.strptime(startinput,'%Y-%m-%d %H:%M:%S').timetuple())
    end = time.mktime(datetime.strptime(endinput,'%Y-%m-%d %H:%M:%S').timetuple())

    who = input('please input the name of the people:')
    location = input('please input the location:')
    content = input('please input the content:')

    # add appointment in calendar
    apt_1 = appointment(start,end,who,location=location,content=content)
    Cal = calendar()
    Cal.add_appointment(apt_1)

    #check conflict
    start_2 = start +1
    end_2 = end -1
    apt_2 = appointment(start_2,end_2,who)
    Cal.add_appointment(apt_2)

    #check name
    Cal.checkname(who)

    #check time
    Cal.checktime(start)

main()