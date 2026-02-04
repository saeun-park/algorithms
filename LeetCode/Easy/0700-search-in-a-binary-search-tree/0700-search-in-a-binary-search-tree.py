# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.bst(root, val)

    def bst(self, node, val):
        if node is None:
            return 
        if node.val == val:
            return node
        if node.val > val:  
            return self.bst(node.left, val)
        if node.val < val:
            return self.bst(node.right, val)
 