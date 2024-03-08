class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations)

        while l <= r:
            mid = (l + r) // 2
            val = bisect_left(citations, mid)
            size = len(citations) - val
            
            if mid <= size:
                l = mid + 1
            elif mid > size:
                r = mid - 1
        return r
    
        
       