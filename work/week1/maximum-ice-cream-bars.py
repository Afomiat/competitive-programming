class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_val = max(costs)
        min_val = min(costs)
        count = [0] * (max_val - min_val + 1)
       
        for cost in costs:
            count[cost - min_val] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]
        sorted_costs = [0] * len(costs)

        for i in reversed(costs):
            sorted_costs[count[i - min_val] - 1] = i
            count[i - min_val] -= 1
        print(sorted_costs)
        c = 0
        for i in sorted_costs:
            if coins - i >=0:
                coins-=i
                c += 1

        return c
       
        