class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
   
        if left > len(nums) - 1 or left < 0:
            return [-1, -1]
        if nums[left] != target:
            left = -1
        if nums[right - 1] != target:
            right = 0
  
        return  [left, right - 1]