a = int(input())
q = a
sq = a*a
s = 0
while(q!=0):
    r = q%10
    s = s*10+r
    q = q//10
    if q == 0:break
revsq = s*s
s1 = 0
while(revsq!=0):
    r1 = revsq%10
    s1 = s1*10+r1
    revsq= revsq//10
if sq == s1:
    print("True")
else:
    print("False")