from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1)) # 뒤집어야함 
            graph[b].append((a, 0)) # 그대로 냅둠

        visited = [False]*n
        
        def dfs(node):
            visited[node] = True
            cnt = 0

            # 반복문으로 노드 연결
            # visited 처리
            # 방향 바꿔야하는 경우에 cnt 더해가기
            for next_node, direction in graph[node]:
                if not visited[next_node]:
                    cnt += direction
                    cnt += dfs(next_node)

            return cnt
        return dfs(0)