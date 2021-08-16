# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:13:58 2018

@author: wangruixuan_sx
"""
import pandas as pd
import numpy as np
#from scipy import stats
import matplotlib.pyplot as plt
import os
from datetime import datetime

#from scipy.optimize import curve_fit
#设定显示语言为中文
import pylab
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
pylab.mpl.rcParams['axes.unicode_minus'] = False

def getFileNames(file_path, sort = False, dir_name = False):
    """
    用于获取一个文件路径下的文件和文件夹（可选）
    
    参数
    -----------------------------------------
    file_path:文件路径，字符串
    sort:逻辑变量，表示是否将获取的文件排序，默认为False
    dir_name:逻辑变量，表示是否获取该路径下的文件夹，默认为False
    """
    file_names = []
    dir_names = []
    for root,dirs,files in os.walk(file_path):
        for i in files:
            file_names.append(i)
            
            if sort == True:
                file_names_out = list(np.sort(file_names))
            else:
                file_names_out = file_names
                
        if dir_name == True:
            for j in dir_names:
                dir_names.append(j)
            return(file_names_out, dir_names)
        else:     
            return file_names_out



def num2Datetime(date_num):
    """
    此函数用于将%Y%m%d整数格式的日期序列转化为datetime类型的日期列表
    
    参数
    -------------------
    date_num: %Y%m%d整数格式的日期序列
    """
    date_datetime = []
    date_num = pd.Series(date_num)
    date_str = pd.DataFrame.astype(date_num, dtype = "str")
    for _ in date_str:
        date_datetime.append(datetime.strptime(_, "%Y%m%d"))
    return(date_datetime)

def datetime2Num(datetime):
    """
    此函数用于将datetime类型的日期序列转化为%Y%m%d整数格式日期列表
    
    参数
    -------------------
    datetime: datetime型的日期
    """
    date_num = []
    datetime_s = pd.Series(datetime)
    date_str = pd.DataFrame.astype(datetime_s, dtype = "str")
    for _ in date_str:
        _new = ''
        for j in range(3):
            _new += _.split('-')[j]
        
        date_num.append(int(_new))

    return(date_num)




def datetime2Str(datetime):
    """
    此函数用于将datetime类型的日期序列转化为%Y%m%d整数格式日期列表
    
    参数
    -------------------
    datetime: datetime型的日期
    """
    import ruixuan
    date_str = []
    datetime_s = pd.Series(datetime)
    date_str_df = pd.DataFrame.astype(datetime_s, dtype = "str")
    
    date_str = ruixuan.df2List(date_str_df)
    return(date_str)




#写一个小函数
def data2DataHist(data):
    """
    此函数用于将绘制折线图的数据转化为绘制直方图的数据
    
    参数
    -------------
    data：用于绘制折线图的数据，DataFrame格式
    """
    data_hist = []
    price = data.index.values 
    volume = data.volume.values
    for i in range(len(price)):
        if volume[i] != 0:
            for j in range(int(volume[i])):
                data_hist.append(price[i])
        else:
            pass
#    data_hist = pd.DataFrame(data_hist)
    return(data_hist)
    
    


def date2Datetime(day):
    '''
    将数字格式的日期转化成datetime格式
    '''
    year_0 = str(day)[:4]
    month_0 = str(day)[4:6]
    day_0 = str(day)[6:]
    date = datetime.strptime(year_0 +"-" + month_0 + "-" + day_0, "%Y-%m-%d")
    return (date, year_0, month_0, day_0)



def time2Datetime(data):
    '''
    将数字格式的时间转化为datetime格式
    
    -------------------
    data：某一天的数字格式的时间
    '''
    import ruixuan
    datetime_list = []
    [date, year_0, month_0, date_0] = ruixuan.date2Datetime(data.date[0])
    for time in data.time:
        hour = str(time)[:-7]
        minute = str(time)[-7:-5]
        second = str(time)[-5:-3]
        
        time_str = year_0 + "-" + month_0 + "-" + date_0 + "-" + hour + "-" +\
                                            minute + "-" + second
        time_datetime = datetime.strptime(time_str, "%Y-%m-%d-%H-%M-%S")
        datetime_list.append(time_datetime)
    datetime_pd = pd.DataFrame(datetime_list, columns = ["datetime"])
    return(datetime_pd)       

    

def df2List(df):
    """
    DataFrame格式向list格式转变
    """
    ls = []
    for i in range(len(df)):
        ls.append(df.values[i][0])
    return(ls)
    
def reindex(df):
    df.index = range(len(df))
    return(df)
