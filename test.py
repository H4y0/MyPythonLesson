a=[x for x in range(2,501) if not [y for y in range(2,x) if x%y == 0]]
print(a[-1])