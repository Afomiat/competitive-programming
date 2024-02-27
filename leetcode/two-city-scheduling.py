class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
       
        arr = []
        res = 0
        for a, b in costs:
            arr.append([b - a, a, b])
        arr.sort()
        for i in range(len(arr)):
            if i < len(arr) // 2:
                res += arr[i][2]
            else:
                res += arr[i][1] 
        return res