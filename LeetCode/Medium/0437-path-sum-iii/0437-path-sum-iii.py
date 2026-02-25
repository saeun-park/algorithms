class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def count(node, curr_sum):
            cnt = 0
            if not node:
                return 0
            
            # 루트에서 시작해서 현재 노드까지의 경로 합이 target인 경우만 셈.
            curr_sum += node.val
            if curr_sum == targetSum:
                cnt += 1
            
            cnt += count(node.left, curr_sum)
            cnt += count(node.right, curr_sum)
            return cnt

        def dfs(node):
            if not node:
                return 0
            return count(node, 0) + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

            
