class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        min_val = 0
        max_val = max(heaters[-1], houses[-1])
        

        def helper(mid):
            ht, hs = 0, 0
            while hs < len(houses) and ht < len(heaters):
                l = heaters[ht] - mid
                r = heaters[ht] + mid
                if houses[hs] >= l and houses[hs] <= r:
                    hs += 1
                else:
                    ht += 1
            return hs == len(houses)

        while min_val <= max_val:
            mid = (min_val + max_val) // 2

            if helper(mid):
                max_val = mid - 1
                ans = mid

            else:
                min_val = mid + 1
        return ans
