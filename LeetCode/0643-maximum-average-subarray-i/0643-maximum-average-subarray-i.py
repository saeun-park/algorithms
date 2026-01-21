class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        pre = sum(nums[0:k]) # 최댓값
        maxnum = pre

        for i in range(len(nums)-k):
            pre = pre-nums[i]+nums[i+k]
            if pre >= maxnum:
                maxnum = pre

        return maxnum / k
