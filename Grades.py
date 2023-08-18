a,b,c,d,e = map(int,input().split())
x = (a+b+c+d+e)/5
if(x>=90):
    print("Grade A")
elif(x>=80 and x<90):
    print("Grade B")
elif(x>=70 and x<80):
    print("Grade C")
elif(x>=60 and x<70):
    print("Grade D")
elif(x>=40 and x<60):
    print("Grade E")
else:
    print("Grade F")