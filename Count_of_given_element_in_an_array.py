n = int(input())
l = list(map(int,input().split()))
x = int(input())
c = 0
for i in range(n):
    if x==l[i]:
        c = c+1
print(c)