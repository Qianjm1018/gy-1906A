# def ys(n1,n2):
#     print(n1,'+',n2,'=',n1+n2)
#     print(n1,'-',n2,'=',n1-n2)
#     print(n1,'*',n2,'=',n1*n2)
#     if(n2 != 0):
#         print(n1,'/',n2,'=',n1/n2)
#     else:
#         print('除数不能为0')
# with open("D:\\software data\\pycharm\\gy-1906-1\\demo\\day04\\yunsuan.txt") as h:
#     x=h.readlines()
#     for line in x:
#         line=line.replace('\n','')
#         line_ys=line.split(',')
#         ys(int(line_ys[0]),int(line_ys[1]))

#实现两数相加
# def sum(a,b):
# #     c=a+b
# #     print(a,'+',b,'=',c)
# #     return c
# # #实现两数相减
# # def j(a,b):
# #     c=a-b
# #     print(a,'-',b,'=',c)
# #     return c
# # #实现两数相乘
# # def ch(a,b):
# #     c=a*b
# #     print(a,'*',b,'=',c)
# #     return c
# # #实现两数相除
# # def chu(a,b):
# #     c=a/b
# #     if(b==0):
# #         print('除数不能为0')
# #         return c
# #     else:
# #         print(a, '/', b, '=', c)
# #         return c
# # chu(9,3)
# # chu(ch(18,3),3)

#有参数 有返回值
def h(m,n):
    return '{}中午吃了{}'.format(m,n)
print(h('小h','炸鸡'))
def i(q,c):
    return '{q1}晚上要吃{c1}'.format(c1=c,q1=q)
print(i('哈哈','火锅'))

#未知问题，读取路径及连接数据库是可用try，except，（finally必定执行）