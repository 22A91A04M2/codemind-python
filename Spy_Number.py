a = int(input())
q = a
s = 0
p = 1
while(q!=0):
    r = q%10
    s = s+r
    p = p*r
    q = q//10
    if q==0:break
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")