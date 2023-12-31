class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # my_dict = Counter(nums)
        # op = 0

        # if all( nums[0] == nums[i] for i in range(len(nums))):
        #     return 0
        # else:
        #     nums.sort()
            
        #     i = 0
        #     l = len(nums)
        #     while l > 0:
        #         if len(set(nums)) == 1:
        #             break
        #         min_num = nums[0]
        #         count = my_dict[min_num]
        #         op += l - count
        #         nums = nums[count :]
        #         l -= count
            

        # return op
       


        my_dict = Counter(nums)
        op = 0

        if all(nums[0] == nums[i] for i in range(len(nums))):
            return 0
        else:
            sorted_nums = list(my_dict.keys())
            sorted_nums.sort()

            i = 0
            l = len(nums)

            while l > 0:
                if len(sorted_nums) == 1:
                    break
                min_num = sorted_nums[i]
                count = my_dict[min_num]
                op += l - count
                l -= count
                i += 1

            return op