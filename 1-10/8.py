# -*- coding:utf-8 -*-
'''
输出99乘法表
'''
for i in range(1, 10):
    print
    for j in range(1, i + 1):
        print "%d * %d = %d " % (j, i, i * j),  # 最后这个逗号有意思
