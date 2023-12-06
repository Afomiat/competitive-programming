# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         result = ['']*len(s)
#         ans = ''
#         i = 0
#         for idx in indices:
#             result.insert(idx,s[i])
#             i += 1
#         for char in result:
#             ans += char
        
#         return ans
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        i = 0

        for idx in indices:
            result[idx] = s[i]
            i += 1

        return ''.join(result)