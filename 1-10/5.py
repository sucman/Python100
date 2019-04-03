# -*- coding:utf-8 -*-
'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。


a = int(raw_input("第一个数："))
b = int(raw_input("第二个数："))
c = int(raw_input("第三个数："))
i = 0

if a > b:
    i = a
    a = b
    b = i

if a > c:
    i = c
    c = a
    a = i

if b > c:
    i = c
    c = b
    b = i

print a, b, c

'''
l = []
for i in range(0, 3):
    a = int(raw_input("请输入数字："))
    l.append(a)
l.sort(reverse=True)  # reverse=True降序  reverse=False升序  排序

print l
