class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        count = 0
        count_res = []
        lower, upper = [], []
        stack = []
        res = []
        for i in range(len(s)):
            if not stack and s[i] == '*':
                continue
            elif not stack and s[i] == '|':
                temp = i
                stack.append(s[i])
            elif s[i] == '|' and stack[-1] == '*':
                lower.append(temp)
                upper.append(i)
                count_res.append(count)

                count = 0
                stack = []
                stack.append(s[i])
                temp = i
            elif stack[-1] == '|' and s[i] == '|':
                temp = i
                continue
            else:
                stack.append(s[i])
                count += 1
        # print(count_res)
        for i in range(len(count_res)):
            if i > 0:
                count_res[i] += count_res[i - 1]
     
        for a, b in queries:
            val_1 = bisect_left(lower, a)
            val_2 = bisect_right(upper, b)
            # print(val_1, val_2)
            if (val_2 - val_1) < 1:
                res.append(0)
            elif val_1 == 0:
                res.append(count_res[val_2 - 1])
            else:
                res.append(count_res[val_2 - 1] - count_res[val_1 - 1])
                
           
            
      
        return res