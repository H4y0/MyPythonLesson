import random
import string
from collections import Counter
s=string.ascii_letters+string.digits+string.punctuation
l=[random.choice(s) for i in range(1000)]
d=Counter(l)
print(d.most_common())
