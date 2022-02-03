input_ = '1321131112'

def number(nb, time):
    a = 0
    while a<time:
        for i in range(len(nb)):
            if i == 0:
                w = ''
                v = nb[i]
                c = 0
            if nb[i] == v:
                c += 1
            if nb[i] != v:
                w += str(c) + v
                v = nb[i]
                c = 1
            if i == len(nb)-1:
                w += str(c) + v
        nb = w
        a += 1
    return w
print(len(number(input_, 50)))