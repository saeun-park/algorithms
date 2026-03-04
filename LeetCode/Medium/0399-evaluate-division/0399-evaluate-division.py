from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        visited = set()
        resultList = []

        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
        
        def dfs(curNode, targetNode, res):
            visited.add(curNode)
            if curNode==targetNode:
                return res

            for nextNode, weight in graph[curNode]:
                if nextNode not in visited:
                    result = dfs(nextNode, targetNode, weight*res)
                    if result != -1:
                        return result
            return -1
        
        for a, b in queries:
            if a not in graph or b not in graph:
                resultList.append(-1.0)
            else:
                visited = set()
                resultList.append(dfs(a, b, 1))
        
        return resultList