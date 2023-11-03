r,c = map(int,input().split())
m = []
for il in range(r):
    il = list(map(int,input().split()))
    m.append(il)
s = 0
s1 = 0
for i in range(r):
    for j in range(c):
        if i%2==0:
            s = s+m[i][j]
        else:
            s1 = s1+m[i][j]
print(s,s1)