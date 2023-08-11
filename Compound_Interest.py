#import math
p = int(input())
r = int(input())
t = int(input())
# n = int(input())
c = p*pow((1+r/100),t)-p
# c = p(1+r/n)**(n*t)
print(f"{c:.2f}")