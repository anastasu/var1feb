f = open('26.txt')
n = int(f.readline())
e = []
o = set()
for i in range(n):
    x = int(f.readline())
    if x % 2 == 0:
        e.append(x)
    else:
        o.add(x)
k = 0
m = 0
ee = set(e)
for i in range(len(e)-1):
    for j in range(i+1, len(e)):
        sr = (e[i] + e[j]) // 2
        if sr in ee or sr in o:
            k += 1
            if sr > m:
                m = sr
print(k, m)