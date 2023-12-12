class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n != 1:
            sqrt_sum = 0
            n_list = list(map(int,str(n)))
            for i in n_list:
                sqrt_sum += i**2
            n = sqrt_sum
            if n == 4:
                return False
        return True


        