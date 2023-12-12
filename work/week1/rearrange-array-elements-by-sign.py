class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # odd_ arr.append odds
        # for nums if num =  even append else odd.apend
        odd_arr = []
        even_arr = []
        result = []
        
        for num in nums:
            if num  < 0:
                odd_arr.append(num)
            else:
                even_arr.append(num)
        for i in range(len(odd_arr)):
            result.append(even_arr[i])
            result.append(odd_arr[i])
        return result

    