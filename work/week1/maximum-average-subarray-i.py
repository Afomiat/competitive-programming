class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
   
        n = len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(n - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

        


        
