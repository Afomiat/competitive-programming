class Solution:
    def maxScore(self, s: str) -> int:
        one_pref = list(map(int, s))
        zero_pref = [bit ^ 1 for bit in one_pref]
        n = len(zero_pref)
        _sum = 0
        _max = float('-inf')
        for i in range(n):
            _sum += one_pref[i]
            one_pref[i] = _sum
        _sum = 0
        print(zero_pref)
        for i in range(n):
            _sum += zero_pref[i]
            zero_pref[i] = _sum
            print(zero_pref[i])
       
        for i in range(n - 1):
            val = zero_pref[i] + (one_pref[n - 1] - one_pref[i])
            _max = max(_max, val) 
            
        return _max