class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count_dict = Counter(arr)

        perc = (25 * len(arr))/100
        # loop through and add ele to dict

        for key , value in count_dict.items():
            if value > perc:
                return key