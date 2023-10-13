n = int(input())
l = list(map(int,input().split()))
se=0
so=0
for i in range(n):
    if i%2==0:
        se+=l[i]
    elif i%2!=0:
        so+=l[i]
print(abs(so-se))