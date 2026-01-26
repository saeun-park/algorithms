# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leaf1 = []
        leaf2 = []
        
        self.dfs(root1, leaf1)
        self.dfs(root2, leaf2)

        return leaf1 == leaf2

    def dfs(self, node, leaves):
        if node is None:
            return 
        if node.left is None and node.right is None:
            leaves.append(node.val)
            return

        self.dfs(node.left, leaves)
        self.dfs(node.right, leaves)
                