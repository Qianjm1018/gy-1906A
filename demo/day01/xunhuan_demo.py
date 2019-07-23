#100以内的所有质数
#1为质数，2位合数(n)
for m in range(2,100):
    n=1
    for i in range(2,m):
        if(m%i ==0):
          n=2
    if(n == 2):
        print(m,"为合数")
    else:
        print(m,"为质数")
#99乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print(b,"×",a,"=",a*b,'\t',end='')
    print()

