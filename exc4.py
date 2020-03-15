import math
sc = input()
s = sc.split()
#num = [int(x) for x in s]
num = list(map(int,s))    
ave = sum(num)/len(s)
avf = sum((float(i)-ave)**2 for i in s)/len(s)
avb = math.sqrt(avf)
s.sort()
if len(s)%2!=0:
    mid = s[int(len(s)/2)]
else:
    mid = (s[int(len(s)/2)+s(len(s)/2-1)])/2
s.sort()
print("平均值{} 方差{} 标准差{} 中位数{}".format(ave,avf,avb,mid))