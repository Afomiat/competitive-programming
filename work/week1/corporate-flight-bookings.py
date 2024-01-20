class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 1)
        
        for a, b, k in bookings:
            prefix[a - 1] += k 
            prefix[b] -= k
        for i in range(1, n + 1):
            prefix[i] = prefix[i -1] + prefix[i]
        prefix.pop()
        return prefix