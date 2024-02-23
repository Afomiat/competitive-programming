class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        my_set = set()
        stack = []
        my_dict = {}
        
        for i in range(len(s)):
            my_dict[s[i]] = i
        for i in range(len(s)):
            if s[i] in my_set:
                continue
            while stack and stack[-1] > s[i] and my_dict[stack[-1]] > i:
             
                    my_set.remove(stack[-1])
                    stack.pop()
               
            stack.append(s[i])
            my_set.add(s[i])
            
        
        return ''.join(stack)