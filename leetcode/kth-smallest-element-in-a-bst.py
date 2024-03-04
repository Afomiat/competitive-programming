# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def helper(root):
            if not root:
                return 
            res.append(root.val)
            helper(root.left)
            helper(root. right)
            return

        helper(root)
        res.sort()
        
        return res[k - 1]