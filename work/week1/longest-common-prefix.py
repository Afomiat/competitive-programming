class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        ans = ""
        for l in range(len(base)):
            for word in strs[1:]:
                print(word)
                if l == len(word) or base[l] != word[l]:
                    return ans
                    # l == len(word) or 
            ans+=base[l]
        return base
        