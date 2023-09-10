n = int(input())
q = n
s = 0
s1=0
while(q!=0):
    r = q%10
    s = s*10+r
    q = q//10
    if q == 0:break
if s==n:
    print("True")
else:
    print("False")