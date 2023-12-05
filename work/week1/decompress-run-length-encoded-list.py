class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        l, r = 0, 1
        result = []

        while True:
            if r >= len_nums:
                break
            else:
                for _ in range(nums[l]):
                    result.append(nums[r])
            l += 2
            r += 2

        return result

        


        

