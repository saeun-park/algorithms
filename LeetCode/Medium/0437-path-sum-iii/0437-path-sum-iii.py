class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        
        # 이 노드에서 시작해서 아래로 내려가며 targetSum인 경로 세기
        def count_from(node, remaining):
            if not node:
                return 0
            
            count = 0
            remaining -= node.val
            
            if remaining == 0:  # 여기까지 합이 딱 targetSum
                count += 1
            
            # 더 아래로 내려가봄 (0 되고도 더 갈 수 있음)
            count += count_from(node.left, remaining)
            count += count_from(node.right, remaining)
            return count
        
        # 모든 노드를 시작점으로 시도
        result = count_from(root, targetSum)        # root에서 시작
        result += self.pathSum(root.left, targetSum)  # 왼쪽 노드들에서 시작
        result += self.pathSum(root.right, targetSum) # 오른쪽 노드들에서 시작
        return result