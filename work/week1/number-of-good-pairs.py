class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        l = 0
        # nums.sort()
        count = 0
        for r in range(len(nums)):
            if nums[r] in d:
                count += d[nums[r]]
                d[nums[r]] += 1
            else:
                d[nums[r]] = 1
          
        return count
        

            # {
            #     1:2,
            #     2:1,
            #     3:2,

            # }
            # ans += 1 + 2 + 1