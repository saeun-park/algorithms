class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = nums[0]
        n = len(nums)

        for i in range(n-1):
            if nums[i+1] != nums[i]+1:
                if start == nums[i]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i]}")

                start = nums[i+1]

        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res