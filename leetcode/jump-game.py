class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
     
        for i in range(len(nums)):
            if len(nums) > 1 and step < (len(nums) - 1):
                step = max(step, i + nums[i])
                if step == i:
                    return False
        return True

           
