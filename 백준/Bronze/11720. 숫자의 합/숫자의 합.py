n = int(input())
nums = int(input())
nums_str = str(nums)

s = 0
for num in nums_str:
    s += int(num)
    
print(s)