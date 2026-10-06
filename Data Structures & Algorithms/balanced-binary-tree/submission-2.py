# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True

        def dfs(root):
            if not root:
                return 0
            if not self.res:
                return -1
            right = dfs(root.right)
            left = dfs(root.left)

            if abs(left - right) > 1:
                self.res = False
            if not self.res:
                return -1
            return 1+ max(left, right)
        dfs(root)
        return self.res