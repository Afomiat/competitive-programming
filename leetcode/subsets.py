class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(idx, path):
            if idx > len(nums):
                return
            
            res.append(path[:])
                
            for i in range(idx, len(nums)):
                path.append(nums[i])
                helper(i + 1, path)
                path.pop()
        helper(0, [])
        return res