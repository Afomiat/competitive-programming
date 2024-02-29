# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(r1,r2):
            if not r1 and not r2:
                return
            if r1 and r2:
                r1.val = r1.val + r2.val
            if not r2:
                return r1
            if not r1:
                return r2
               

            left = helper(r1.left, r2.left)
            r1.left = left
            right = helper(r1.right, r2.right)
            
            r1.right = right
            return r1
        
        
        return helper(root1, root2)