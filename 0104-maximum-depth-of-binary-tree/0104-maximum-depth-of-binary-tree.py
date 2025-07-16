class Solution:
    def maxDepth(self, root): 
        # 트리가 비어있다면 깊이는 0
        if not root:
            return 0
        
        # 왼쪽 서브트리의 최대 깊이를 재귀적으로 계산
        left_depth = self.maxDepth(root.left)
        # 오른쪽 서브트리의 최대 깊이를 재귀적으로 계산
        right_depth = self.maxDepth(root.right)
        
        # 현재 노드의 깊이는 (왼쪽 또는 오른쪽 서브트리 중 더 깊은 값) + 1
        return max(left_depth, right_depth) + 1