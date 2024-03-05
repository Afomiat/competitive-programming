class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(path, idx):
            
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path[:])
                return
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                helper(path, i)
                path.pop()

        helper([], 0)
        return res