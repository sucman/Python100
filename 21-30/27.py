# -*- coding:utf-8 -*-
'''
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''


def op(s, l):
    if l == 0:
        return
    print (s[l - 1])
    op(s, l - 1)


s = raw_input("请输入字符串：")
l = len(s)
op(s, l)
