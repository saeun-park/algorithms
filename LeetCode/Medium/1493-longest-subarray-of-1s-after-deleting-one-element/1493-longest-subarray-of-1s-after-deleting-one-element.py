class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, zero_cnt, max_len = 0, 0, 0
        if sum(nums)==n:
            return n-1

        for right in range(n): # 오른쪽 포인터
            if nums[right]==0:
                zero_cnt += 1
            
            while zero_cnt >= 2:
                if nums[left]==0:
                    zero_cnt -= 1

                left += 1
            max_len = max(max_len, right-left)
        
        return max_len
