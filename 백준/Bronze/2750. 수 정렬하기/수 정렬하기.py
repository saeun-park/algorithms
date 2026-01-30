n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

s = sorted(nums)
for i in s:
    print(i)