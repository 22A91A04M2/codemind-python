s = int(input())
h = s//3600
sec = s - (h*3600)
m = sec//60
secs = sec%60
print("H:M:S-%d:%d:%d"%(h,m,secs))