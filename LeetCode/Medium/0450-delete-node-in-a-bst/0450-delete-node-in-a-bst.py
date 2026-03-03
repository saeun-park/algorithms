# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # root.val == key
            if root.left and root.right:
                # tmp: 오른쪽 서브트리의 root
                tmp = root.right
                # 오른쪽 서브트리의 최소값 찾는 반복문
                while tmp.left:
                    tmp = tmp.left
                # 루트 값을 최소값으로 대체
                root.val = tmp.val
                # tmp.val(삭제해야할 최소값)을 deleteNode 재귀 호출하여 삭제
                root.right = self.deleteNode(root.right, tmp.val)

            elif root.right:
                return root.right
            elif root.left:
                return root.left
            else:
                return None
        
        return root
            
