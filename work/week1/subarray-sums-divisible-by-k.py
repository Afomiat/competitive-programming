class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = 0
        n = len(nums)
        my_dict = {0: 1}
        result = 0

        for i in nums:
            pref += i
            val = pref % k
            if val in my_dict:
                result += my_dict[val]
            my_dict[val] = my_dict.get(val, 0) + 1
        
        return result
