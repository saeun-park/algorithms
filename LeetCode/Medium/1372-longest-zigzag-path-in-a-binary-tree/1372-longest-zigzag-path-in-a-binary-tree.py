# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node, direction, cur_len):
            if not node:
                return 0
            self.max_len = max(self.max_len, cur_len)

            if direction=='l':
                dfs(node.right, 'r', cur_len+1)
                dfs(node.left, 'l', 1)
            else:
                dfs(node.left, 'l', cur_len+1)
                dfs(node.right, 'r', 1)
            
        if root.left:
            dfs(root.left, 'l', 1)
        if root.right:
            dfs(root.right, 'r', 1)

        return self.max_len