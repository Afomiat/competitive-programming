# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
       
        def test(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and not root2:
                return False 
            if root2 and not root1:
                return False
            
            if root1.val != root2.val:
                return False
            
          
            return test(root1.left, root2.left) and test(root1.right, root2.right)
            


        
        return test(p, q)