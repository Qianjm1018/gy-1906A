#a代表变量名=赋值符，表示把右边的值存到左边的变量里
a='keingd'
print(type(a))
#字符串有四种表示方式，"第一种表示方式"，'第二种表示方式'，'''第三种表示方式''''，""第四种表示方式""
#print()在控制台打印，type()显示变量存的数据类型
b=2517
print(type(b))
#[]表示List代表一个列表，可以存多个数据中间用","隔开
c=[1,2,4]
print(type(c))
#()表示tuple代表一个元组，可以存多个数据中间用","隔开
d=(1,4,6)
print(type(d))
#键值对数据 姓名：钱佳敏 电话：18918
#{}表示dict 代表一个字典 ，可以储存多个键值对数据，多个键值对中间用","隔开，key和value中间用":"隔开、
e={"姓名":"钱佳敏","电话":"18918"}
print(type(e))
print(e)

#练习
#第一组数据 张三,李四,王五,赵六,钱七
f=("张三","李四","王五","赵六","钱七")
print(type(f))
#第二组数据 姓名:张三 年龄:18 性别:女 科目:语文 成绩:80
g={"姓名":"张三","年龄":18,"性别":"女","科目":"语文","成绩":80}
print(type(g))
#第三组数据 A,2,3,4,5,6,7,8,9,J,Q,K
h=("A",2,3,4,5,6,7,8,9,"J","Q","K")
print(type(h))
#第四组数据 10000
i=10000
print(type(i))
#第五组数据 学生
j="学生"
print(type(j))