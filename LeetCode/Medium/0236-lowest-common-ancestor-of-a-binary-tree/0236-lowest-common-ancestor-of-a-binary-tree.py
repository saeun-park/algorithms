class Solution:
    # LCA는 p와 q가 갈라지는 최초의 지점이다.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==p or root==q or root is None:
            return root
        # 각 서브트리에서 p나 q를 찾으면 그 노드를 반환
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 왼쪽에서 p를 찾고 오른쪽에서 q를 찾았으면 둘 다 None이 아니다.
        # 그 말은 즉 p와 q가 서로 다른 서브트리에 있다는 뜻
        # 그 상태에서의 root는 p와 q가 갈라지는 최초 지점이다.
        if left and right:
            return root
        # right에서 아무것도 못 찾으면 lca는 아직 위에 있을 것임.
        if left:
            return left
        return right
        
        