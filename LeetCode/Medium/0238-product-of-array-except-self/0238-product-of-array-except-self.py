class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        left, right = 1, 1

        for i in range(n):
            if i>=1:
                left = left*nums[i-1]
            answer[i] = left
        
        for i in range(n-1, -1, -1):
            if i<n-1:
                right = right*nums[i+1]
            
            answer[i] = answer[i]*right
        
        return answer
