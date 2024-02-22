class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        count = 0
        for i in logs:
            if stack and i == '../':
                stack.pop()
            elif i == './':
                continue
            elif i == 'x/':
                count += 1
            elif i != '../' and i != './' and i != 'x/':
                stack.append(i)
        return len(stack) + count