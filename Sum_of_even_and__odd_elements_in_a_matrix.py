r,c = map(int,input().split())
s = 0
o = 0
m = []
for i in range(r):
    il = list(map(int,input().split()))[:c:]
    m.append(il)
for il in m:
    for j in il:
        if j%2==0:
            s+=j
        else:
            o+=j
print(f"{s} {o}")