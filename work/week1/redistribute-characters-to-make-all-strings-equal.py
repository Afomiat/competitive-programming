class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        my_list = []
        for word in words:
            for s in word:
                my_list.append(s)
        my_dict = Counter(my_list)
        for val in my_dict.values():
            if val % len(words) != 0:
                return False
       
        return True