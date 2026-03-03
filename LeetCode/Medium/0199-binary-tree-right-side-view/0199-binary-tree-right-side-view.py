from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        # while 한 번 = 한 레벨 처리
        while q:
            level_size = len(q)
            # 해당 레벨의 노드 수만큼 반복
            for i in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                if i==level_size-1:
                    res.append(node.val)
        return res


        