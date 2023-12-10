class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(word) for word in words)
        
        result = []
        for i in range(max_length):
            current_word = ""
            for word in words:
                current_word += word[i] if i < len(word) else ' '
            result.append(current_word.rstrip())
        
        return result


