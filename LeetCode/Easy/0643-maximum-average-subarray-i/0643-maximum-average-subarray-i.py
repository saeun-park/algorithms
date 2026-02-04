class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window = sum(nums[0:k]) # 최댓값
        maxnum = window

        for i in range(len(nums)-k):
            window = window-nums[i]+nums[i+k]
            if window >= maxnum:
                maxnum = window

        return maxnum / k
