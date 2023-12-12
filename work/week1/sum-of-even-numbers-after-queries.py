class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        final = []
        even_sum = sum(num for num in nums if num % 2 == 0)

        for query in queries:
            val, index = query
            old_val = nums[index]

            if old_val % 2 == 0:
                even_sum -= old_val

            new_val = old_val + val
            nums[index] = new_val

            if new_val % 2 == 0:
                even_sum += new_val

            final.append(even_sum)

        return final
