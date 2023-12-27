class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(0,n - i -1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # result = []
        # my_dict = Counter(nums)
       
        # for j in range(len(my_dict)):
        #     min_key = min(my_dict, key = int)
        #     for i in range(my_dict[min_key]):
        #         result.append(min_key)
        #     del my_dict[min_key]
        # nums = result
            
       