class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
    
        def sPop(s):
            result = []
            for i in range(len(s)):
                s_pop = s.pop()
                result.append(s_pop)

            s.extend(result)
        sPop(s)           
        
        # s.reverse()
            