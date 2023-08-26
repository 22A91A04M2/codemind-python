m= int(input())
n= int(input())
for i in range(m,n+1):
    flag = True
    j=i
    while(j!=0):
        r = j%10
        j = j//10
        if r!=0 and i%r!=0:
            flag = False
            break   
    if flag==True and i%10!=0:
        print(i,end = " ")
