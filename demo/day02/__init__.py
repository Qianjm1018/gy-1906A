# a="uiwngidnankw2dkn"
# print(a[0:2])
# print(a[6:7])
# print(a[5:11])
# print(a[-6:-4])
# print(a[-3:-2])
# print(a[-9:-5])

#按照扑克牌的规则，现在有6张牌，只要5张
#黑桃（S）红桃（H）方块（D）梅花（C）
#牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
#数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
#[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
a='''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
a = a[1:-1]
print(a)
#字符串切片方法
qi=a.split("', '")
print(qi)
print(type(qi))
b="""[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']"""
print(b)
j=b.replace("''",'''"''')

print(j)
print(type(j))