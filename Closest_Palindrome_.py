def ispal(n):
    k = n
    ans = 0
    while(k):
        r = k%10
        ans = ans*10+r
        k = k//10
    return(ans == n)


n = int(input())
x = 1
flage = False
ans1 = -1 
ans2 = -1
while(True):
    if(ispal(n+x) == True and ispal(n-x) == True):
        ans1 = x+n
        ans2 = n-x
        flage = True
        break
    elif(ispal(n+x) == True):
        ans1 = n+x
        break
    elif(ispal(n-x) == True):
        ans1 = n-x
        break
    x+=1
if(flage == True):
    print(ans2,ans1)
else:
    print(ans1)