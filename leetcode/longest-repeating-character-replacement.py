class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len, max_val = 0, 0
        my_dict = {}
        while r < len(s):
            val = s[r]
            my_dict[val] = my_dict.get(s[r], 0) + 1
            max_val = max(max_val, my_dict[val])
            while (r - l + 1) - max_val > k:
                my_dict[s[l]] -= 1
                l += 1 
            max_len = max(max_len, r - l + 1)

            r += 1
        
        return max_len