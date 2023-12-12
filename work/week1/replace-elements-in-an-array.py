class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        # separate operations first ,last

        # for i in nums if first in nums : nus[i] = last[first.indx(i)]
        my_dict = {}
        result = []
        count = 0
        for i in range(len(nums)):
            my_dict[nums[i]] = i
            count += 1

        for oper in range(len(operations)):
            first, last = operations[oper]
            if first in my_dict:
                idx = my_dict[first]
                nums[idx] = last
                my_dict[last] = idx
                del my_dict[first]
                
        return nums

            # for key, value in my_dict.items():
            #         if key == first:
            #             key = last
        # for key in my_dict:
        #     result.append(key)
        

      
       