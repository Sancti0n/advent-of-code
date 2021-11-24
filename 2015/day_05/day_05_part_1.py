import re

with open('2015/day_05/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

voyelles = ['a','e','i','o','u']
interdits = ['ab','cd','pq','xy']
doubles = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
count = 0
t = []
voyelles_re = re.compile("|".join(voyelles))
interdits_re = re.compile("|".join(interdits))
doubles_re = re.compile("|".join(doubles))
for i in range(len(lines)):
    if not interdits_re.search(lines[i]) and doubles_re.search(lines[i]):
        if voyelles_re.search(lines[i]):
            for a in range(len(voyelles)):
                count += len(re.findall(voyelles[a], lines[i]))
            if count >= 3:
                t.append(lines[i])
                count = 0
            else: count = 0
print(len(t))