from json import loads

with open('2015/day_12/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

def nombre(elt):
    if type(elt) == int:
        return elt
    if type(elt) == list:
        return sum([nombre(j) for j in elt])
    if type(elt) != dict:
        return 0
    if 'red' in elt.values():
        return 0
    return nombre(list(elt.values()))

print(nombre(loads(lines[0])))