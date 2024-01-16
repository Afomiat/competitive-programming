class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        my_sum = 0
        result = []
        for i in nums:
            my_sum += i
            result.append(my_sum)

        return result

