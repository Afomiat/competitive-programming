class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        vis = set()
        def helper(path):
            
            if len(nums) == len(path):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in vis:
                    path.append(nums[i])
                    vis.add(nums[i])
                    helper(path)
                    path.pop()
                    vis.remove(nums[i])
               
            
        helper([])
        return res