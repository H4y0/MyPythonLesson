import string
import random
s=string.ascii_letters+string.digits+string.punctuation
lst=[random.choice(s) for i in range(100)]
d={}
for i in lst:
    d[i]=d.get(i,0)+1
t=list(d.items())
t.sort(key=lambda i:i[1],reverse=True)
t[:10]