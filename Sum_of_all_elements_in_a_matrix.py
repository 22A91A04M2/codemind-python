r,c = map(int,input().split())
mat = []
for i in range(r):
    l = list(map(int,input().split()))[:c:]
    mat.append(l)
s = 0
for l in mat:
    for e in l:
        s += e
print(s)