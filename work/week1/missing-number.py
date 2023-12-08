class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #  find number of list
        #  for the range of list if that number not in list return it
        for num in range(0, len(nums) + 1):
            if num not in nums:
                return num