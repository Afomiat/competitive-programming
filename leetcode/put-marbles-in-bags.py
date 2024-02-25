class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        res = []
        
        for i in range(len(weights) - 1):
            res.append(weights[i] + weights[i + 1])
        res.sort()
        min_sum = 0
        max_sum = 0
        for i in range(k - 1):
           
            min_sum += res[i]
            max_sum += res[len(weights) - i - 2]
      

        return max_sum - min_sum