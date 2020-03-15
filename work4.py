import jieba
import string
with open("诗词.txt","r",encoding="utf-8") as f:
    txt=f.read()
lst=jieba.lcut(txt)

d={}
for i in lst:
    if len(i)==1:
        continue
    else:
        d[i]=d.get(i,0)+1
t=list(d.items())
t.sort(key=lambda i:(i[1],i[0]),reverse=True)
print(t[:])