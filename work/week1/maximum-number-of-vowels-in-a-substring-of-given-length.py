class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v_counter = Counter(s[:k])
        max_v = 0
       
      
        for i in range(len(s) - k + 1):
            my_sum = 0
            for key, val in v_counter.items():
                if key in ['a', 'e', 'i', 'o', 'u']:
                    my_sum += val
        
            max_v = max(max_v, my_sum )
            v_counter[s[i]] -= 1
            if v_counter[s[i]] == 0:
                del v_counter[s[i]]
            if i + k < len(s):
                if s[i + k] not in v_counter:
                    v_counter[s[i + k]] = 1
                else:
                    v_counter[s[i + k]] += 1

       

        
        return max_v