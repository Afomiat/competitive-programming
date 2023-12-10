class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = ''
        st = 0
        new_str += s[:spaces[st]] + " " 
        i = 0
        while st < len(spaces)-1:
            new_str += s[spaces[st + i]:spaces[st+ i + 1]] + " " 
            st += 1
        new_str += s[spaces[st]:] 
        return new_str
