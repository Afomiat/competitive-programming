# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
                if node is None:
                    return None
                
                if node.val == p.val or node.val == q.val:
                    return node
                
                left = helper(node.left)
                right = helper(node.right)
                
                if left and right:
                    return node
                elif left:
                    return left
                else:
                    return right

        return helper(root)