n = int(input())
q= n
s = 0
while(q!=0):
    r = q%10
    s = s*10+r
    q = q//10
ans = 0
x = 1
while s:
    r = s%10
    ans+=r**x
    x =x+1
    s = s//10
print(ans == n)