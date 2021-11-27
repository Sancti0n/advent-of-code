import re
import string

with open('2015/day_05/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

t = list(string.ascii_lowercase)

tab = []
for i in range(len(lines)):
    for a in range(len(t)):
        if re.search(t[a]+'[^.]'+t[a]+']*', lines[i]):
            for b in range(len(t)):
                for c in range(len(t)):
                    if len(re.findall(t[b]+t[c], lines[i])) >= 2:
                        tab.append(lines[i])

print(len(set(tab)))