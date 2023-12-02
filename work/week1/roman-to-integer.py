class Solution:
    def romanToInt(self, s: str) -> int:
        dict ={'I':1, 'V':5, 'X':10,
                    'L':50, 'C':100, 'D':500, 'M':1000}
        pre_value = 0
        final = 0
        for i in s:
            value = dict[i]
            if value > pre_value:
                final += value - (2*pre_value)
            else:
                final += value
            pre_value = value
        return final

