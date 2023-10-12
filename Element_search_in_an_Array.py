n = int(input())
nums = list(map(int,input().split()))
se = int(input())
is_found=False
for i in nums:
    if i == se:
        is_found = True
        break
print(is_found)