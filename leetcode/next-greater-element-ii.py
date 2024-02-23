class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
       
        for i  in range(2*n):
           
            while stack and nums[i%n] > stack[-1][0]:
                val, idx = stack.pop()
                res[idx] = nums[i%n]
                
            stack.append([nums[i%n], i%n])
      
        return res

       