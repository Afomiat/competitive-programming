# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums):
            if not nums:
                return None
            max_val = max(nums)
            idx = indexOf(nums, max_val)
            root = TreeNode(max_val)
            root.left = helper(nums[:idx])
            root.right = helper(nums[idx + 1:])
            return root
        return helper(nums)