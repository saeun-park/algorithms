class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
         
        for i in range(1, numRows):
            prev = res[-1]
            middle = []

            for j in range(len(prev)-1):
                middle.append(prev[j]+prev[j+1])

            res.append([1] + middle + [1])

        return res