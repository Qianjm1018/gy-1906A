#小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟
a=20
if(a>=10):
    print(a,"元可以买红双喜")
if(a>=25):
    print(a, "元可以买玉溪")
if(a>=5):
    print(a, "元可以买大前门")
#成人票 200 未成年100元 12岁以下的小孩票100 60岁以上的老人票 150 小明今年18岁，去买票应该买哪种票？
a=18
if(a>=18 and a<60):
    print(a,"买成人票")
elif(a<=12):
    print(a,"买小孩票")
elif(a>=60):
    print(a,"买老人票")
elif (a<18 and a>12):
    print(a, "买未成年票")
# 打印出100以内奇数
for i in range(100):
    if (i % 2 == 1):
        print(i)