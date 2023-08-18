u = int(input())
if u<=199:
    c = 1.20
elif u>=200 and u<400:
    c = 1.40
elif u>=400 and u<600:
    c = 1.60
elif u>=600 and u<800:
    c = 1.80
else:
    c = 2.00
b = u*c
if b>400:
   s = 0.15*b
else:
    s = 0
cb = b+s
print("Units Consumed: %d"%(u))
print("Cost per Unit: %0.2f"%(c))
print("Bill: %0.2f"%(b))
print("Surcharge: %0.2f"%(s))
print("Total Amount: %0.2f"%(cb))