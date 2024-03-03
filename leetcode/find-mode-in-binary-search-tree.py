# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(root):
            if root == None:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
            return
        helper(root)
        ans = []
        count = Counter(res)
        max_val = max(count.values())
        for key, val in count.items():
            if val == max_val:
                ans.append(key)

        return ans