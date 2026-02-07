class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right, zero_cnt, max_len = 0, 0, 0, 0
    
        while right <= n-1:
            if nums[right] == 0:
                zero_cnt += 1
            right += 1
            
            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            max_len = max(max_len, right-left)
        return max_len
