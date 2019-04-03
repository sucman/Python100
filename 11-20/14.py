# -*- coding:utf-8 -*-
'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
'''

a = int(raw_input("请输入数字："))
print "{} = ".format(a),

while a not in [1]:  # 循环保证递归
    for index in xrange(2, a + 1):
        if a % index == 0:
            a = a / index
            if a == 1:
                print index
            else:  # index 一定是素数
                print "{} *".format(index),
                break

'''
def test(a):
    print "{} = ".format(a),
    if not isinstance(a,int) or a <= 0:
        print "请输入正确数字。"
        exit(0)
    elif a in [1]:
        print "{} = ".format(a)
    while a not in [1]:# 循环保证递归
        for index in xrange(2, a +1):
            if a % index == 0:
                a = a / index
                if a == 1:
                    print index
                else:# index 一定是素数
                    print "{} *".format(index),
                    break
test(123)
'''
