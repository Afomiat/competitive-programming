class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # has to be consecutive
        # the numbers are less than the input number
        if num % 3 != 0:
            return []
        a = num//3
        return [a-1,a,a+1]