a = int(input())
b = int(input())
f = 0
g = 0
for i in range(1,a):
    if (a%i==0):
        f = f+i
for i in range(1,b):
    if b%i==0:
        g = g+i
if g==a and f==b:
    print("Amicable")
else:
    print("Not Amicable")