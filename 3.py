n=int(input())
for i in range(n):
    a=int(input())
    a1=a//10
    a2=(a-a1*10)//5
    a3=(a-a1*10-a2*5)
    print("{} = {}*10 + {}*5 + {}*1".format(a,a1,a2,a3))