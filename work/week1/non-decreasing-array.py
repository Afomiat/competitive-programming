class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        # if sorted(nums) == nums:
        #     return True
        # else:
        count = 0
        # for num in range(len(nums)-1):
        #     if nums[num] < nums[num+1]:
        #         pass
        #     else:
        #         count += 1
        # return True if count <= 1 else False
                
            # min_nums= min(nums)
            # first = min_nums - 1
            # nums[0] = first
            
            # if sorted(nums) == nums:
            #     return True
            # else:
            #     return False
    
        from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for num in range(len(nums)-1):
            if nums[num] > nums[num+1]:
                count += 1
                if count > 1:
                    return False
                
                if num > 0 and nums[num-1] > nums[num+1]:
                    nums[num+1] = nums[num]
                else:
                    nums[num] = nums[num+1]
        return True

