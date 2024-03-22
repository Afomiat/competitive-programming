class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        check = [i for i in range(1, len(nums) + 1)]
        nums = set(nums)
      
        res = []
        for i in check:
            if i not in nums:
                res.append(i)
            
        return res
