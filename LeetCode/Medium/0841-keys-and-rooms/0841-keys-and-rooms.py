class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def dfs(loc):
            visited.add(loc)
            for key in rooms[loc]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == len(rooms)