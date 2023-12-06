class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict = {}
        result = []
        #  if length of list < 3 then return the list
        if len(nums) < 3:
            return set(nums)

        #  else declare dictionary and initialize it to one each elements
        #  if  n/3 == dict[key] then return the key
        else:
            for num in range(len(nums)):
                if nums[num] in dict:
                    dict[nums[num]] += 1
                else:
                    dict[nums[num]] = 1
            for key, value in dict.items():
                if value > len(nums)/3:
                    result.append(key)

            # for num in range(len(nums)):
            #     if dict[nums[num]] > len(nums)/3:
            #         result.append(nums[num])

            return result
