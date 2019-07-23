'''
字典的特性
1、字典中的key唯一
            不允许同一个键出现两次。创建时如果同一个键要被赋值两个次，后一个值会被记住
2、key是不可改变的 数字，字符串，元组
            元组(1,2,45,36)可以作为key，但是(1,[3])不可以作为一个key

'''
#增
#字典新增一对数据
a={}
a["姓名"]='qjm'
print(a)
a[3]=122
print(a)
a[(1,2)]=2333
print(a)
#删
#pop参数只能为key
a.pop(3)
print(a)
del a['姓名']
print(a)
#清空字典
a.clear()
print(a)
#改
a["姓名"]='jm'
print(a)
#查
#根据key查看value
print(a["姓名"])
#遍历字典(借助循环)
for key in a:
    print(a[key])
#字典合并
k={"姓名":'kek'}
w={"性别":'女'}
k.update(w)
print(k)
#两个字典合并，生成一个新的字典
print(dict(k,**w))
print(k)
print(w)
#成员判断(key)
#获取字典长度