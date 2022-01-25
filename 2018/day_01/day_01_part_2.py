with open('2018/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
t = [0]
value = True
while value:
    for i in range(len(lines)):
        v += int(lines[i].split('\n')[0])
        if v in t: 
            print(v)
            value = False
        else:
            t.append(v)

# Version optimisée avec cycle
'''
import itertools
with open('2018/day_01/list.txt', encoding="utf-8") as f:
    nums = f.readlines()

for i in range(len(nums)):
    nums[i] = int(nums[i].split('\n')[0])

print(f"Part 1: {sum(nums)}")

freqs ={0}

for f in itertools.accumulate(itertools.cycle(nums)):
    if f in freqs:
        print(f"Part 2: {f}")
        break
    freqs.add(f)
'''