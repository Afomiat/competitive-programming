class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        maxi = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            maxi = max(maxi,r-l+1)
        return maxi

        # j, i = 0, 1
        # maxi = 0
        # while i < len(s) and j < i:
        #     window = s[j:i]
        #     if len(window) == len(set(window)):
        #         i += 1
        #         maxi = max(maxi, len(window))
        #     else:
        #         j += 1
        #         i += 1
        # return maxi

        