class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        count = 0
        for r in ranges:
            
            for t in range(r[0],r[1]+1):
                covered.add(t)
                

        for i in range(left, right + 1):
            if i not in covered:
                return False
                
           
        return True