n = int(input())
l = list(map(int,input().split()))
so=0
se=0
for i in range(n):
    if l[i]%2!=0:
        so+=l[i]
    elif l[i]%2==0:
        se+=l[i]
print(abs(so-se))