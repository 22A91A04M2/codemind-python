n = int(input())
x = list(map(int,input().split()))
s = sum(x)//n
print(s in x)