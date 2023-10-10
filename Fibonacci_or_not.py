import math
def persq(x):
    s = int(math.sqrt(x))
    return s*s == x
n = int(input())
a = (5*n*n)+4
b = (5*n*n)-4
if persq(a) or persq(b):
    print("True")
else:
    print("False")