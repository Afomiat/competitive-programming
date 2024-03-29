class Solution:
    def largestGoodInteger(self, num: str) -> str:

        max_good_integer = ""
        
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                current_good_integer = num[i:i+3]
                if current_good_integer > max_good_integer:
                    max_good_integer = current_good_integer
        
        return max_good_integer

