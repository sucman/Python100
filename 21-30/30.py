# -*- coding:utf-8 -*-
'''
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

a = int(raw_input("请输入数字："))
x = str(a)
flag = True

for i in range(len(x) / 2):
    if x[i] != x[-i - 1]:
        flag = False
        break

if flag:
    print "%d 是一个回文数。" % a
else:
    print "%d 不是回文数。" % a
