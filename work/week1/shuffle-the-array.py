class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        result = []
        first_half = []
        second_half = []
        # split the array in half and store them in separate arrays
        for num in range(n):
            first_half.append(nums[num])

        for num in range(n,len(nums)):
            second_half.append(nums[num])

        # iterate  for both array and append them in a new array
        for num in range(n):
            result.append(first_half[num])
            result.append(second_half[num])
        
        return result