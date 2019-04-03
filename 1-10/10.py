# -*- coding:utf-8 -*-
'''
暂停一秒输出，并格式化当前时间。
  
%a 星期几的简写;如 星期三为Web 
%A 星期几的全称;如 星期三为Wednesday 
%b 月份的简写; 如4月份为Apr 
%B 月份的全称; 如4月份为April 
%c 标准的日期的时间串;（如： 04/07/10 10:43:39） 
%C 年份的后两位数字 
%d 十进制表示的每月的第几天 
%D 月/天/年 
%e 在两字符域中，十进制表示的每月的第几天 
%F 年-月-日 
%g 年份的后两位数字，使用基于周的年 
%G 年分，使用基于周的年 
%h 简写的月份名 
%H 24小时制的小时 
%I 12小时制的小时 
%j 十进制表示的每年的第几天 
%m 十进制表示的月份 
%M 十时制表示的分钟数 
%n 新行符 
%p 本地的AM或PM的等价显示 
%r 12小时的时间 
%R 显示小时和分钟：hh:mm 
%S 十进制的秒数 
%t 水平制表符 
%T 显示时分秒：hh:mm:ss 
%u 每周的第几天，星期一为第一天 （值从0到6，星期一为0） 
%U 第年的第几周，把星期日做为第一天（值从0到53） 
%V 每年的第几周，使用基于周的年 
%w 十进制表示的星期几（值从0到6，星期天为0） 
%W 每年的第几周，把星期一做为第一天（值从0到53） 
%x 标准的日期串 
%X 标准的时间串 
%y 不带世纪的十进制年份（值从0到99） 
%Y 带世纪部分的十制年份 
%z，%Z 时区名称，如果不能得到时区名称则返回空字符。 
%% 百分号
---------------------

'''

import time

print time.strftime("%a", time.localtime(time.time()))  # %a星期几的简写
print time.strftime("%A", time.localtime())  # %A星期几的全称

print time.strftime("%b", time.localtime())  # %b月份的简写
print time.strftime("%B", time.localtime())  # %B 月份的全称

print time.strftime("%c", time.localtime())  # %c 标准的日期的时间串;（如： 04/07/10 10:43:39）
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 格式化的时间串

print time.strftime("%d", time.localtime())  # %d 十进制表示的每月的第几天

'''
format
print time.strftime("%C",time.localtime()) # %C 年份的后两位数字
print  time.strftime("%D",time.localtime())# %D 月/天/年
print time.strftime("%F") # %F 年-月-日
print time.strftime("%e",time.localtime()) # %e 在两字符域中，十进制表示的每月的第几天
'''
