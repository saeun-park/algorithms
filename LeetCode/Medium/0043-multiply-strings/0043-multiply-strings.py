class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)-1
        l2 = len(num2)-1
        res = [0]*(len(num1)+len(num2))

        for i in range(l1, -1, -1):
            for j in range(l2, -1, -1):
                a = int(num1[i]) if i>=0 else 0
                b = int(num2[j]) if j>=0 else 0
                
                s = (a*b)+int(res[i+j+1])
                res[i+j+1] = s % 10
                res[i+j] += s // 10

        result = "".join(map(str, res))
        
        idx = 0
        while idx < len(res) and res[idx]==0:
            idx += 1

        return "".join(map(str, res[idx:])) if idx<len(res) else '0'

