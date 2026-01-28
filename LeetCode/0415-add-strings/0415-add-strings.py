class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i = len(num1)-1
        j = len(num2)-1
        carry = 0

        while i>=0 or j>=0:
            a = int(num1[i]) if i>=0 else 0
            b = int(num2[j]) if j>=0 else 0
            s = a + b + carry
            res.append(str(s%10))
            carry = s//10

            i -= 1
            j -= 1
        if carry:
            res.append(str(1))
        return "".join(res[::-1])