class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        max_size = float('-inf')

        for trip in trips:
            max_size = max(max_size, trip[2])
        prefix = [0] * (max_size + 2)

        for k, a, b in trips:
            prefix[a] += k
            prefix[b] -= k
        for i in range(1, max_size):
            prefix[i] = prefix[i - 1] + prefix[i]
        print(prefix)

        return all( x <= capacity for x in prefix)