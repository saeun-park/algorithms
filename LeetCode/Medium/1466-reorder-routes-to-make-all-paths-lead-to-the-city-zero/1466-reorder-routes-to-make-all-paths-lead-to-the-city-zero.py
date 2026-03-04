from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in connections:
            # direction = 1  → 이 방향 그대로 두면 0으로 못 감 → 바꿔야 함
            graph[a].append((b, 1))
            # direction = 0  → 이미 0쪽으로 갈 수 있음 → 그대로
            graph[b].append((a, 0))

        visited = [False]*n
        
        def dfs(node):
            visited[node] = True
            cnt = 0

            # 반복문으로 노드 연결
            # visited 처리
            # 방향 바꿔야하는 경우에 cnt 더해가기
            for next_node, direction in graph[node]:
                if not visited[next_node]:
                    cnt += direction # direction이 1인 경우에 뒤집어야 하므로
                    cnt += dfs(next_node)

            return cnt
        return dfs(0)