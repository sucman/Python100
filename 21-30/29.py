# -*- coding:utf-8 -*-
'''
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
x = int(raw_input("请输入一个不多于5位的正整数："))
a = x / 10000
b = x % 10000 / 1000
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10

if a != 0:
    print "五位数", e, d, c, b, a
elif b != 0:
    print "四位数", e, d, c, b
elif c != 0:
    print "三位数", e, d, c
elif e != 0:
    print "两位数", e, d
else:
    print "一位数", e
