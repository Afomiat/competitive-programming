from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_one = Counter(ransomNote)
        count_two = Counter(magazine)
        
        for key, val in count_one.items():
            if key not in count_two or val > count_two[key]:
                return False
        
        return True