#1
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上：{}，向下：{}".format(dayup,daydown))
#2
def day(f):
    return pow(1+f,365)
print(day(0.01))
print(day(-0.01))
print(day(0.005))
print(day(-0.005))
#3
dayup = 1.0
for i in range(365):
    if i%7 in [0,6]:
        dayup = dayup*(1-0.01)
    else:
        dayup = dayup*(1+0.01)
print(dayup)
#4
def dc(f):
    days = 1.0
    for i in range(365):
        if i%7 in [0,6]:
            days = dayup*(1-0.01)
        else:
            days = dayup*(1+0.01)
    return days
df = 0.01
while dc(df)<37.18:
    df+=0.01
print(df)