# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = ''
        res = 0
        def helper(root, ans):
            nonlocal res
            if not root:
                return
         
            if not root.left and not root.right:
                res += int(ans + str(root.val))
                return 
            helper(root.left, ans + str(root.val))
            helper(root.right, ans + str(root.val))
            return
           
        helper(root, ans)
        return res