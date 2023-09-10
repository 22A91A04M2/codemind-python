a = int(input())
q = a
s = 0
while(q!=0):
    r = q%10
    s = s*10+r
    q = q//10
    if q==0:break
print(s)