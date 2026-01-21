class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        pre = sum(nums[0:k]) # 최댓값
        maxnum = pre

        for i in range(len(nums)-k):
            cur = pre-nums[i]+nums[i+k]
            pre = cur
            if cur >= maxnum:
                maxnum = cur

        return maxnum / k