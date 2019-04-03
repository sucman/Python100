# -*- coding:utf-8 -*-
'''
利用递归方法求阶乘
'''


def fac(x):
    if x == 0:
        sum = 1
    else:
        sum = x * fac(x - 1)
    return sum


print fac(x=int(raw_input("请输入数字：\n")))
