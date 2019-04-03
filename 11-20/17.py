# -*- coding:utf-8 -*-
'''
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
a = raw_input("请输入字符串：\n")
letter = 0
space = 0
digit = 0
other = 0
for b in a:
    if b.isalpha():
        letter += 1
    elif b.isspace():
        space += 1
    elif b.isdigit():
        digit += 1
    else:
        other += 1

print "char = %d,space = %d,digit = %d,other = %d" % (letter, space, digit, other)
