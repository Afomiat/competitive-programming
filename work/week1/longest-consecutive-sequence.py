class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_cons = 1

        for num in num_set:
            if num - 1 not in num_set:  
                cur_num = num
                cur_cons = 1

                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_cons += 1

                max_cons = max(max_cons, cur_cons)

        return max_cons
