# -*- coding:utf-8 -*-
'''
求1+2!+3!+...+20!的和。
'''
s = 1
m = 0

for i in range(1, 21):
    s = s * i
    m = m + s
print "1!+2!+3!+...+20!的和等于：", m
