# -*- coding:utf-8 -*-
'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
juli = []
gaodu = []

qishi = 100.0  # 起始高度
cishu = 10  # 次数

for i in range(1, cishu + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        juli.append(qishi)
    else:
        juli.append(2 * qishi)
    qishi /= 2
    gaodu.append(qishi)

print ("总距离：juli = {0}".format(sum(juli)))
print ("第10次反弹高度：gaodu = {0}".format(gaodu[-1]))
