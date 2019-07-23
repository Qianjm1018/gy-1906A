#! /usr/bin/env python
# -*- coding: utf-8 -*-


'''
按照扑克牌的规则，现在有6张牌，只要5张
黑桃（S）红桃（H）方块（D）梅花（C）
牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
'''
# a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
# # #字符串的替换
# a = a.replace("''",'"')
# #字符串截取
# a = a[2:-2]
#
# print(a)
#
# #字符串的切片方法
#
# b = a.split('" , "')
#
# print(b)
#
# #key 唯一；并且存一对数据
# #key存牌的大小，value存key出现的次数
# #{'1':3,"10":1,"7":2}
# d={}
# for i in b:
#     c = i[1:]
#     if(c in d ):
#         d[c] +=1
#     else:
#         d[c]  =1
# print(d)
# bool2 = False  # 字典KEY的值为2的时候为True
# bool3 = False  # 字典KEY的值为3的时候为True
# for key in d:
#     if(d[key]==3):
#         bool3 = True
#     if(d[key]==2):
#         bool2 = True
# if(bool2  and bool3):
#     print("可以三带二")
# else:
#     print("不可以")
# m='''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
# m=m[2:-2]
# c=m.split('" , "')
# print(c)


#def是方法定义的关键字，juge_3_2()方法名，可自定义不可以数字开头，
def juge_3_2(a):
    #第一步：统一符号  对字符串的处理，用replace（）
    #a='''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
    #a= input("请输入牌型：")
    a=a.replace("''",'"')
    #print(a)
    # 第二步：去掉中括号 字符串截取  [::]
    a=a[2:-2]
    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    b=a.split('" , "')
    #print(b)
    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    #for key in b:
        #print(key[1:])
    # 第五步：统计相同的数字个数  用字典去统计
    d={}
    for c in b:
        y=c[1:]
        if y in d:
            d[y] += 1
        else:
            d[y]  =1
    print(d)
    # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    m1=0#字典KEY的值为2的时候为1
    m2=0#字典KEY的值为3的时候为1
    for key in d:
        if(d[key] == 2):
            m1=1
        if(d[key] == 3):
            m2=1
    if(m1==1 and m2==1):
        print("3带2")
    else:
        print("不可3带2")


# for i in range(3):
#     juge_3_2(i)
# with open("D:\\software data\\pycharm\\gy-1906-1\\demo\\day04\\cards.txt",'r') as h:
#     x=h.readlines()
#     for e in x:
#         e=e.replace("\n",'')
#         print(e)
#         juge_3_2(e)
#






















with open("cards.txt",'r')as m:
    line=m.readlines()
    for lines in line:
        lines=lines.replace("\n",'')
        print(lines)
        juge_3_2(lines)
