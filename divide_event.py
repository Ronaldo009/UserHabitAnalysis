# -*- coding: utf-8 -*-
# 时间    : 2018/10/13 17:20
# 作者    : xcl

#用水事件划分
import pandas as pd

threshold = pd.Timedelta('4 min') #阈值为分钟
inputfile = 'C:\\Users\\Administrator\\Desktop\\UserHabitAnalysis\\data/water_heater.xls' #输入数据路径,需要使用Excel格式
outputfile = 'C:\\Users\\Administrator\\Desktop\\dividsequence.xls' #输出数据路径,需要使用Excel格式

data = pd.read_excel(inputfile)
data[u'发生时间'] = pd.to_datetime(data[u'发生时间'], format = '%Y%m%d%H%M%S')
data = data[data[u'水流量'] > 0] #只要流量大于0的记录
d = data[u'发生时间'].diff() > threshold #相邻时间作差分，比较是否大于阈值
data[u'事件编号'] = d.cumsum() + 1 #通过累积求和的方式为事件编号

data.to_excel(outputfile)

#print(d)