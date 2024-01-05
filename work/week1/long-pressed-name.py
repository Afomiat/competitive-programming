class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l, r = 0, 0

        while l < len(name) and r < len(typed):
            if name[l] == typed[r]:
                l += 1
                r += 1
            elif r > 0 and typed[r] == typed[r - 1]:
                r += 1
                
            else:
                return False

        while r < len(typed) and typed[r] == typed[r - 1]:
            r += 1

        return l == len(name) and r == len(typed)