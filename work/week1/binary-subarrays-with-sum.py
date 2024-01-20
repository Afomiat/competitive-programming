class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict = {0:1}
        pref = 0
        result = 0
        for i in nums:
            pref += i
            val = pref - goal
            
            result += my_dict.get(val, 0) 
            my_dict[pref] = my_dict.get(pref, 0) + 1
        
        return result