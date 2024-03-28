class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        my_set = set()
        def prime(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    n //= d
                    my_set.add(d)
                d += 1
            if n > 1:
                my_set.add(n)
            return

        for i in nums:
            prime(i)
        return len(my_set)