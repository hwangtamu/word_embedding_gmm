# get test data
import re
from collections import Counter
p = 'data/wiki_00'
q = 'data/vocab.txt'
o = 'data/test_words.txt'
a = []
b = []
with open(q, 'r') as file:
    for i in file:
        b += [i.split()[0].strip()]

b = set(b)

with open(p, 'r') as f:
    tmp = []
    for i in f:
        if bool(re.search(r'<.+>', i)):
            if len(tmp)>0:
                a+=[tmp]
            tmp = []
        if not bool(re.search(r'<.+>', i)):
            tmp += re.findall(r'[A-Za-z]+', i.strip().lower())

out = []
for i in a:
    if len(set(i)-b)>2:
        a = set(i)-b
        tmp = {}
        for w in a:
            tmp[w] = i.count(w)
        t = Counter(tmp).most_common(1)
        if t[0][1]>2 and len(i)<200:
            out += [t[0][0], ' '.join(i)]

with open(o, 'w') as output:
    output.writelines('\n'.join(out))

