class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        res = 0
        
        while target > 1 and maxDoubles > 0:
            if target % 2:
                res += 2
            else:
                res += 1
            target = target // 2
            maxDoubles -= 1

        return res + target - 1


