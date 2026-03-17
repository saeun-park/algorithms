from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int: 
        m, n = len(maze), len(maze[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        q = deque()
        r, c = entrance[0], entrance[1]
        q.append((r, c, 0))
        # visited = [[False]*n for _ in range(m)]
        visited = []
        for _ in range(m):
            visited.append([False]*n)

        while q:
            r, c, dist = q.popleft()
            visited[r][c] = True

            for x, y in directions:
                nr = r+x
                nc = c+y

                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] =='.' and not visited[nr][nc]: # 이동 가능한 경우
                    if nr == m-1 or nc == n-1 or nr==0 or nc==0: # border인 경우
                        if (nr, nc) != entrance:
                            return dist+1 
                    else:
                        visited[nr][nc] = True
                        q.append((nr, nc, dist+1))
                
        return -1

            
