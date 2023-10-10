n = input()
l1 = len(n)
l2 = len(set(n))
if l1==l2:
    print("Unique Number")
else:
    print("Not Unique Number")