class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        my_dict ={0 : 1}
        n = len(nums)
        pref = 0
        for i in nums:
            pref += i
            val = pref - k
            if val in my_dict:
                result += my_dict[val]
            my_dict[pref] = my_dict.get(pref, 0) + 1

        return result
