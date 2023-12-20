class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        my_dict = {}
        
        for num in range(len(nums)):
            if nums[num] not in my_dict:
                my_dict[nums[num]] = [num]
            else:
                my_dict[nums[num]].append(num)

        if all(len(val) < 2 for val in my_dict.values()):
            return 0

        count = 0
        for values in my_dict.values():
            for i in range(len(values)):
                for j in range(i + 1, len(values)):
                    if values[i] * values[j] % k == 0:
                        count += 1
                        
        return count