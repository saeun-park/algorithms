class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False

        str_x = str(abs(x))
        reverse_x = str_x[::-1]
        return x==int(reverse_x)