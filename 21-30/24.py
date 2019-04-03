# -*- coding:utf-8 -*-
'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。
    b = i
    i = i + j
    j = b
'''
a = 2.0
b = 1.0
s = 0
for i in range(1, 21):
    s += a / b
    j = a
    a = a + b
    b = j
print s

c = 2.0
d = 1.0
s = 0
for a in range(1, 21):
    s += c / d
    c, d = c + d, c
print s

e = 2.0
f = 1.0
l = []
l.append(e / f)
for a in range(1, 20):
    e, f = e + f, e
    l.append(e / f)
print reduce(lambda x, y: x + y, l)
