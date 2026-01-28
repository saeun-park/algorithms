class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        half_n = len(nums)/2
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1

            if d[num] > half_n:
                return num

        