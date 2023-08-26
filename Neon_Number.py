a = int(input())
b = a*a
q = b
s = 0
while(q!=0):
    r = q%10
    s = s+r
    q = q//10
    if q == 0:break
if(a==s):
    print("Neon Number")
else:
    print("Not Neon Number")