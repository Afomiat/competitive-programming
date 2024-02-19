class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = set()

        for i in range(n):
            if i not in visited:
                visited_cycle = set()
                while True:
                    if i in visited_cycle:
                        return True
                    visited.add(i)
                    visited_cycle.add(i)

                    prev, i = i, (i+nums[i])%n
                    if prev == i:
                        break
                    if nums[prev] > 0 and nums[i] < 0:
                        break
        return False                

       