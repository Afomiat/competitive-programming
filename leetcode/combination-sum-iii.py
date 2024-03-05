class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def helper(first, path):
            vis = set()
            if len(path) == k and sum(path) == n:
                res.append(path[:])
                return
            elif len(path) == k:
                return

            for i in range(first, 10):
                if i not in vis:
                    path.append(i)
                    vis.add(i)
                    helper(i + 1, path)
                    path.pop()
                    vis.pop()
        helper(1,[])
        return res