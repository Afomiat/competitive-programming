class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = float('-inf')
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                max_one = max(max_one,count)
                count = 0
        max_one = max(max_one, count)

        return max_one
