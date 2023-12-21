class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        result = []
        for digit in digits:
            s += str(digit)
        s = int(s) + 1
        s = str(s)
        for i in range(len(s)):
            result.append(int(s[i]))
        return result
