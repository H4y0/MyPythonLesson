lst = input()
lst = "".join([x for x in lst if x not in '1234567890.' and x not in '-' and x not  in '...'])
lst2 = list(lst.split())
for x in lst2:
    if x.startswith('#')==True:
        lst2.remove(x)
    elif x.startswith('@')==True:
        lst2.remove(x)
res = "".join(str(x) for x in lst2)
if len(res)==0:
    print("none")
else:
    for x in res:
        print(x,end=" ")