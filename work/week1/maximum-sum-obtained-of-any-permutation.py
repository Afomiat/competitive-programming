class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pref = [0] * n

        for a, b in requests:
            pref[a] += 1
            if b + 1 < n:
                pref[b + 1] -= 1

        for i in range(1, n):
            pref[i] += pref[i - 1]

        pref.sort(reverse=True)
        nums.sort(reverse=True)

        result = 0
        mod = 10**9 + 7

        for i in range(n):
            result = (result + pref[i] * nums[i]) % mod

        return result