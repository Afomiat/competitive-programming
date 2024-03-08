class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start, end = [], []
        res = []

        my_dict = {}
        
        for a, b in intervals:
            start.append(a)
            end.append(b)
        for i, a in enumerate(start):
            my_dict[a] = i
        start.sort()
        print(max(start))
        for i in end:
            val = bisect_left(start, i) 
            if val == len(start):
                print(i)
                res.append(-1)
            else:
                print(start[val], i)
                res.append(my_dict[start[val]])
        
     
       
        return res
