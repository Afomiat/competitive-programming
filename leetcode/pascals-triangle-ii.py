class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        pre_val = self.getRow(rowIndex - 1)
        
        for i in range(1, len(pre_val)):
            cur = pre_val[i - 1] + pre_val[i]
            res.append(cur)
        res.append(1)
        return res