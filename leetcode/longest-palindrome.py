class Solution:
    def longestPalindrome(self, s: str) -> int:
        my_dict = Counter(s)
        count = 0
        flag = 0
        if all(c == s[0] for c in s):
            return len(s)
        for val in my_dict.values():
            if val > 1 and val % 2 == 0:
                count += val
            elif val > 1 and val % 2 != 0:
                flag += 1
                count += (val // 2) * 2
            else:
                flag += 1
        if flag > 0:
            count += 1
        return count