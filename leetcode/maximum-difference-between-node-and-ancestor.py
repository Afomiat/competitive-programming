# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [0]
        # max_val = float('')
        def helper(root):
            if not root:
                return
            if not root.left  and not root.right:
                return [root.val, root.val]
            
            left = helper(root.left)
            right = helper(root.right)
            max_val_l, max_val_r  = root.val, root.val
            min_val_l, min_val_r = root.val, root.val


            if left:
                max_val_l = max(left[1], root.val)
                min_val_l = min(left[0], root.val)
            if right:
                max_val_r = max(right[1], root.val)
                min_val_r = min(right[0], root.val)
            
            
            res[0] = max(res[0], abs(root.val - max_val_l), abs(root.val - max_val_r), abs(root.val - min_val_l), abs(root.val - min_val_r))
            
            max_val = max(max_val_l, max_val_r)
            min_val = min(min_val_l, min_val_r)
            
           

            return [min_val, max_val]
        helper(root)

        # print(res)
        return res[0]