# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        my_dict = defaultdict(list)
        key = 1
        def helper(root, key):
            if not root:
                return
            # print(my_dict)
            my_dict[key].append(root.val)
            helper(root.right, key + 1)
            helper(root.left, key + 1)
            
            return

        helper(root, key)
        res = []
        for key, val in my_dict.items():
            if key % 2 != 0:
                res.append(val[::-1]) 
            else:
                res.append(val) 
        return res