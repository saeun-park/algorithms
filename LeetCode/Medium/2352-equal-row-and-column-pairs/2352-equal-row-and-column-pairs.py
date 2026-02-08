class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_count = {}
        for r in range(n):
            t = tuple(grid[r])
            row_count[t] = row_count.get(t, 0) + 1
        
        ans = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            if col in row_count:
                ans += row_count[col]

        return ans