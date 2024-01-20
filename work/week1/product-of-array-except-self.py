class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        post = []
        result = []
        my_sum = 1

        for i in nums:
            my_sum *= i
            pref.append(my_sum)

        my_sum = 1
        for i in reversed(nums):
            
            my_sum *= i
         
            post.append(my_sum)
        post = post[::-1]
        
        for i in range(len(nums)):
            if i != 0 and i != len(nums) - 1:
                mul = pref[i - 1] * post[i + 1]
                result.append(mul)
            elif i == 0:
                result.append(post[i + 1])
            else:
                result.append(pref[i - 1])

        return result