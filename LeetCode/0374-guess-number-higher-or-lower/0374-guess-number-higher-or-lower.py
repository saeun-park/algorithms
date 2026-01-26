# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.set_range(n, 1, n)
        
    def set_range(self, n, left, right):
        mid = int((left+right)/2)

        if guess(mid) == 0:
            return mid
        if guess(mid) == 1:
            left = mid + 1
            return self.set_range(n, left, right)
        if guess(mid) == -1:
            right = mid - 1
            return self.set_range(n, left, right)
