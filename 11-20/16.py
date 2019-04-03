# -*- coding:utf-8 -*-
'''
输出指定格式的日期。
'''
import datetime

# 输出今日日期
print (datetime.date.today().strftime('%d-%m-%Y'))

# 创建日期
a = datetime.date(2032, 1, 5)
print a.strftime('%d-%m-%Y')

# 日期运算
b = a + datetime.timedelta(days=10)
print b.strftime('%d-%m-%Y')

# 日期替换
c = a.replace(year=a.year + 1)
print c.strftime('%d-%m-%Y')
