class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = Counter(nums)

        for key, val in my_dict.items():
            if val > (len(nums)/2):
                return key