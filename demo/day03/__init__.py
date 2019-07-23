a=[1]
#增
a.append(8)
print(a)
b=[5,'idang',2,6,8,7,'idi','i']
print(a+b)
#用exteng合并两个列表
a.extend(b)
print(a)
#删
#根据下标删除某个元素
a.pop(4)
print(a)
#默认删除最后一位元素
a.pop()
print(a)
#清空一个列表
# a.clear()
# print(a)
#改
#根据下标更改某个元素的值
a[2]='das'
print(a)
#查
#根据小标查询某个元素
print(a[5])
#遍历（借助循环）
for m in  a:
    print(m)
#截取
#截取部分数据
print(a[4:6])
#倒序
print(a[::-1])
#隔一个取一个
print(a[::2])
print(len(a))
#成员判断
if(21 in a):
    print('存在列表中')
else:
    print('不存在')