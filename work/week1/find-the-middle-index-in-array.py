class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        cur_val = 0
        prefix = []
        for i in nums:
            cur_val += i
            prefix.append(cur_val)
        
        
        for i in range(len(prefix)):
            if i == 0:
                if 0 == prefix[r] - prefix[i]:
                  
                    return i
            else:
                if prefix[l] == prefix[r] - prefix[i]:
                    return i
                l += 1
        else:
            return -1
