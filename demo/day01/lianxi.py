#成绩0-59不及格，60-70及格 70-80 良好 80以上是优秀    [90,100,81,84]判断下改组成绩是否全部都是优秀
# a=1#1优秀 2不优秀
# for i in[90,100,81,84,45]:
#     if(i<80):
#       a=2
#     if(a==1):
#         print(i,"全都优秀")
#     else:
#         print(i,"不全都优秀")
#"01010010001110001001001010101010010101" 计算下几个0 几个1
# a="01010010001110001001001010101010010101"
# b=0#几个0
# c=0#几个1
# for d in a:
#     if(d=='0'):
#         b=b+1
#     else:
#         c=c+1
# print('有',b,'个0',c,'个1')
#




#1+2+3+4....+100
# a=0
# i=1
# while(i<=100):
#     a=a+i
#     i=i+1
# print(a)
#求出10的阶乘
# a=1
# i=1
# while(i<10):
#    a=a*i
#    i=i+1
# print(a)

# a='http://www.baidu.com/s?word'
# xieyi=a.split('://')[0]
# a=a.split('://')[1]
# print(xieyi)
# ym=a[:a.find('/')]
# print(ym)
# uri=a[a.find('/'):]
# print(uri)


#[开始的位置:截止的位置]
c='https://www.baidu.com/s?ie=UTF-8&wd=python%20%E5%AD%97%E7%AC%A6%E6%88%AA%E5%8F%96'
xy=c.split('://')[0]
c=c.split('://')[1]
print(xy)
ym=c[:c.find('/')]
print(ym)
uri=c[c.find('/'):]
print(uri)






















m='https://www.hao123.com/?tn=92266606_hao_pg'
xym=m.split('://')[0]
m=m.split('://')[1]
print(xym)
ip=m[:m.find('/')]
print(ip)
lj=m[m.find('/'):]
print(lj)













