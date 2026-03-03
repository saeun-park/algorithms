from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        maxSum = root.val
        maxLevel = 1

        while q:
            levelSize = len(q)
            levelSum = 0
            for i in range(levelSize):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level

            level += 1
        
        return maxLevel

        