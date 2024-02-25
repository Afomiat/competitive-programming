class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        res = []
        left_sum = 0
        tot_sum = sum(nums)
        for i, n in enumerate(nums):
            right_sum = tot_sum - n - left_sum
            res.append((i * n ) - left_sum + right_sum - ((len(nums) - 1 - i) * n))

            left_sum += n 
        return res