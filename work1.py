import random
import string

s = string.ascii_letters+string.digits+string.punctuation
lst=[random.choice(s) for i in range(1000)]
d = {}
for i in lst:
    d[i] = d.get(i,0)+1
l = list(d.items())
l.sort(key=lambda i:i[1],reverse=True)
print(l)
