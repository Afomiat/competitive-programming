class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        p_count = Counter(p)
        s_count = Counter(s[:len_p])
        result = []

        for i in range(len_s - len_p + 1):
            if s_count == p_count:
                result.append(i)

            if i + len_p < len_s:
                s_count[s[i]] -= 1
                if s_count[s[i]] == 0:
                    del s_count[s[i]]
                s_count[s[i + len_p]] += 1

        return result