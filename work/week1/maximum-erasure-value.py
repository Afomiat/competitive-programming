class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # n = len(nums)
        # l = 0
        # # window = []
        # my_dict = {}
        # for r in range(n):
        #     window = nums[l:r + 1]
        #     if nums[r] in my_dict:
        #         my_dict[nums[r]] += 1
        #     else:
        #         my_dict[nums[r]] = 1
        #     while my_dict.values > 1 and r < n:
        #         l += 1
        #         del my_dict[nums[l]]
        #         my_dict[nums[r]] = 1
        n = len(nums)
        max_sc = 0
        current_sc = 0
        window = set()
        l = 0

        for r in range(n):
            if nums[r] not in window:
                window.add(nums[r])
                current_sc += nums[r]
                max_sc = max(max_sc, current_sc)
            else:
                while nums[l] != nums[r]:
                    window.remove(nums[l])
                    current_sc -= nums[l]
                    l += 1
                l += 1

        return max_sc