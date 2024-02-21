class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = {}
        end, size = 0, 0
        res = []
        for i in range(len(s)):
           my_dict[s[i]] = i
        for i in range(len(s)):
            size += 1
            end = max(end, my_dict[s[i]])
            if i == end:
                res.append(size)
                size = 0

    
        return res