__author__ = 'Administrator'
# coding=utf-8
import time
def myyear(x):
    if(x%4==0):
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    return months


def aculatedays(x):
    now=time.localtime(time.time())
    print now.tm_year, now.tm_mon,now.tm_mday
    year=int(x[0:4])
    month=int(x[4:6])
    day=int(x[6:8])
    print year,month,day
    sumyear=0
    if month<=now.tm_mon:   #while the month is less than now.month
     while year<now.tm_year: #acculate days by years
        if(year%4==0):
            sumyear=sumyear+366
        else:
            sumyear=sumyear+365
        year=year+1
     summonth=0
     months=myyear(now.tm_year)
     while month<now.tm_mon:  #acculate days by months
        summonth=summonth+months[month-1]
        month=month+1
     sumdays=summonth-day+now.tm_mday+sumyear
     print sumdays

    else:   #while the month is bigger than now.month
      while year<now.tm_year-1:
        if(year%4==0):
            sumyear=sumyear+366
        else:
            sumyear=sumyear+365
        year=year+1
      summonth=0
      months=myyear(year)
      while month<12:
           summonth=months[month-1]+summonth
           month=month+1
      temp=now.tm_mon
      months=myyear(now.tm_year)
      while temp>0:
           summonth=months[temp-1]+summonth
           temp=temp-1
      sumdays=summonth+sumyear+now.tm_mday-day
      print sumdays


aculatedays("20141204")
aculatedays("20140304")
aculatedays("20150304")