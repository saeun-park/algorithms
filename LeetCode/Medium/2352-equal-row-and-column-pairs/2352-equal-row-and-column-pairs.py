class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grid2 = []
        
        for c in range(n):
            li = []
            for g in grid:
                li.append(g[c])
            grid2.append(li)
        
        row_count = {}
        for g in grid:
            t = tuple(g)
            row_count[t] = row_count.get(t, 0)+1

        ans = 0
        for g2 in grid2:
            t = tuple(g2)
            if t in row_count:
                ans += row_count[t]
            
        return ans