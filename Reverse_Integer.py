n=int(input())
t=-n if n<0 else n
s=0
while t:
    r=t%10
    s=s*10+r
    t=t//10
print(-s if n < 0 else s)