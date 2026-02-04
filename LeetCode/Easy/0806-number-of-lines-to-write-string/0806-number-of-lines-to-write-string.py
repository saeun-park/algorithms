class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res = [1, 0]
        x = 0
        
        for c in s:
            index = ord(c) - ord('a')
            if x + widths[index] > 100:
                res[0] += 1
                x = widths[index]
            else:
                x = x + widths[index]
        res[1] = x
        return res
        