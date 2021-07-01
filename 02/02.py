# -*- coding: utf-8 -*-

from datetime import datetime
import calendar

mylist = [] #存日期用

y = input() #年
m = input() #月

#獲取目標月最後一天 
last_day = calendar.monthrange(int(y),int(m))[1]

#每天逐一檢查是不是星期三
for d in range(last_day):
    
    #先把日期轉成一句字串
    date_String = y +"-"+ m + "-" + str(d+1)
    
    #再把字串轉成datetime格式
    target = datetime.strptime(date_String , "%Y-%m-%d")
    
    #檢查是否為星期三(星期日為0，一為1，以此類推)
    if (target.strftime("%w")=='3'):
        mylist.append(str(target)[0:10]) #是的話存起來
    
#印出
for i in range(len(mylist)):
    print(mylist[i])
    
 
# datetime格式的時間轉成str長這樣
# str(target)
# Out[52]: '2020-04-30 00:00:00'

# datetime格式的時間轉成str再擷取部分
# str(target)[0:9]
# Out[53]: '2020-04-3'
    
# calendar.monthrange 用法參考
# In [45]:calendar.monthrange(2021,6)
# Out[45]: (1, 30)
# calendar.monthrange(2021,6)[1]
# Out[46]: 30
# https://www.codenong.com/42950/

# strftime() 用法參考
# https://www.runoob.com/python/att-time-strftime.html