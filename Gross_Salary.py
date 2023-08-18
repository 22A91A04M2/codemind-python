b = int(input())
if(b<=10000):
    d = b*0.8
    h = b*0.2
elif(b<=20000):
    d = b*0.9
    h = b*0.25
else:
    d = b*0.95
    h = b*0.3
g = b+d+h
print(f"{g:.2f}")