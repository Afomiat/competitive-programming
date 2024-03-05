class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
      
        def helper(idx, path,nums):
            if idx > len(nums):
                return 
            res.append(path[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                helper(i + 1, path,nums)
                path.pop()
                
        helper(0, [], sorted(nums))
      
  
        return res