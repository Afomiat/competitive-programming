class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ct = Counter(nums)
        res = 0
        for n in ct:
            tmp = k - n
            if n == tmp:
                res += ct[n] // 2
                continue    
            if n < tmp:
                res += min(ct[n], ct[tmp])
        return res
