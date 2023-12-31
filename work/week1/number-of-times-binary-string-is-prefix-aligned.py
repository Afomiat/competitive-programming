class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        l = len(flips)
        arr = []
        count = 0
        max_index = 0

        for i in range(l):
            max_index = max(max_index, flips[i])
            arr.append(flips[i])

            if max_index == len(arr):
                count += 1

        return count

