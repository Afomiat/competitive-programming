class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,a in enumerate(temperatures):
            while stack and a > stack[-1][0]:
                stack_val,stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append([a,i])
        return res