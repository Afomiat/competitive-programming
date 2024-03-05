class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # my_dict = Counter(candidates)
      
        def helper(idx, path, candidates):
            if idx > len(candidates):
                return
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                helper(i + 1, path, candidates)
                path.pop()
        

        helper(0, [], sorted(candidates))
        return res