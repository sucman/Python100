# -*- coding:utf-8 -*-
'''
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
Sunday，Monday，Tuesday，Wednesday，Thursday，Friday，Saturday
'''

s = raw_input("请输入字符：")

if s == "S":
    se = raw_input("请继续输入：")
    if se == "u":
        print "星期天"
    elif se == "a":
        print "星期六"
    else:
        "无法判断"

if s == "M":
    print "星期一"

if s == "T":
    sec = raw_input("请继续输入：")
    if sec == "u":
        print "星期二"
    elif sec == "a":
        print "星期四"
    else:
        "无法判断"

if s == "W":
    print "星期三"

if s == "F":
    print "星期五"
