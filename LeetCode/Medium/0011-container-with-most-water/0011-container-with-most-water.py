class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        result = 0

        left = 1
        right = n

        while left < right:
            size = (right-left) * min(height[left-1], height[right-1])
            result = max(result, size)

            if height[left-1] > height[right-1]:
                right -= 1
            else:
                left += 1


        return result


        