a = int(input())
if a>1:
    for i in range(2,int(a/2)+1):
        if a%i==0:
            print("not a prime")
            break
    else:
        print("prime")
else:
    print("not a prime")