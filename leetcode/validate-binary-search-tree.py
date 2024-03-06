# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
            return
        helper(root)
       
        # print(res)
        for i in range(len(res)):
            if i > 0:
                if res[i] <= res[i - 1]:
                    
                    return False
        return True