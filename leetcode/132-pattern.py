class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        cur_min = nums[0]

        for i in range(1,len(nums)):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            if stack and nums[i] < stack[-1][0] and nums[i] > stack[-1][1]:
                return True
                
            stack.append([nums[i], cur_min])
            cur_min = min(nums[i], cur_min)
           
       
        return False
                    
