import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
nums_sorted = sorted(nums)
for num in nums_sorted:
    print(num)