# -*- coding:utf-8 -*-
'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
'''
Tx = 0
Sx = []
x = int(raw_input("x = "))
n = int(raw_input("n = "))
for count in range(n):
    Tx = Tx + x
    x = x * 10
    Sx.append(Tx)
    print Tx

Sx = reduce(lambda x, y: x + y, Sx)
print "和为：", Sx
