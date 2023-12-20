class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        my_sum = 0
        my_dict = {}
        maxi = float('-inf')
        result = []
        l_zero_count = 0
        r_one_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                r_one_count += 1
        my_dict[0] = l_zero_count + r_one_count
        for num in range(len(nums)):
            if nums[num] == 0:
                l_zero_count += 1
            else:
                r_one_count -= 1
            my_sum = l_zero_count + r_one_count
            my_dict[num + 1] = my_sum
        for value in my_dict.values():
            maxi = max(maxi, value)
        for key, value in my_dict.items():
            if value == maxi:
                result.append(key)
        return result
