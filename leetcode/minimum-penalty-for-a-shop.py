class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count_Y = 0
        count_N = 0
        min_val = float('inf')
        flag = False
        res = []
        my_dict = Counter(customers)
       

        for i in customers:
            if i == 'Y':
                count_Y += 1
                flag = True
            if flag:
                res.append((my_dict['Y'] - count_Y) + count_N + 1)
                flag = False
            else:
                 res.append((my_dict['Y'] - count_Y) + count_N)
            if i == 'N':
                count_N += 1
        res.append(count_N)
        for i in res:
            min_val = min(min_val, i)
        
        return indexOf(res, min_val)