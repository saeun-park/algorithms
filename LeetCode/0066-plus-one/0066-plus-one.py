class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n):
            digits[i] = str(digits[i])

        str1 = "".join(digits)
        int_digits = int(str1)+1
        str2 = str(int_digits)
        res = [0]*len(str2)
        for i in range(n):
            res[i] = int(str2[i])

        return res


        