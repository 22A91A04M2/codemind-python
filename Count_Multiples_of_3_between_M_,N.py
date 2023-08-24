m,n = map(int,input().split())
c = 0
for i in range(m,n):
    if(i%3==0):
        c = c+1
print(c)