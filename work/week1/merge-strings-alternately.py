class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        min_str =min(len(word1), len(word2))
        for i in range(min_str):
            ans += word1[i]
            ans += word2[i]
        ans += word1[min_str:]
        ans += word2[min_str:]
        return ans























        # # return concatin
        # merged_string = ""
        # for i in range(min(len(word1), len(word2))):
        #     merged_string += word1[i]
        #     merged_string += word2[i]
        
        
        # merged_string += word1[min(len(word1), len(word2)):]
        # merged_string += word2[min(len(word1), len(word2)):]
        
        # return merged_string