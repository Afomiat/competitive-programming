class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0] * (len(s) + 1)
        for a, b, k in shifts:
            n = 1 if k == 1 else -1 
            pref[a] = pref[a] + n
            pref[b + 1] = pref[b + 1] - n
        result = ''
        for i in range(len(s)):
            if i != 0:
                pref[i] = pref[i] + pref[i - 1]
            c = (ord(s[i]) - ord('a') + pref[i]) % 26 + ord('a')
            result += chr(c)
        return result


           