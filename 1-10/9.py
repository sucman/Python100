# -*- coding:utf-8 -*-
'''
暂停0.3秒输出
'''

import time

for i in range(1, 10):
    print
    for j in range(1, i + 1):
        print "%d * %d = %d " % (i, j, i * j),  # 最后这个逗号有意思
        time.sleep(0.3)
