# -*- coding:utf-8 -*-
'''
斐波那契数列
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
'''


def fib(n):
    a = 1
    b = 1

    for i in range(n - 1):
        a, b = b, a + b
    return a


# 输出第8个斐波那契数列
print fib(12)
