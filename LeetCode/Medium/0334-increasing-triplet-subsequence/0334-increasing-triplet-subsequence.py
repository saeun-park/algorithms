class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False
        
        a, b = float('inf'), float('inf')

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True       
        return False