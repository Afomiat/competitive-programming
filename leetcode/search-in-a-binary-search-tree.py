# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
      
        def helper(root, v):
            left = None 
            right = None
      
            if not root:
                return None
            elif root.val == v:
                return root
            elif root.val > v:
                left = helper(root.left, val)
            elif root.val < v:
                right = helper(root.right, val)
           
            if left:
                return left
            else:
                return right
        
        
        return helper(root, val) 
