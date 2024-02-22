class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = list(path.split('/'))
      
        for i in range(len(arr)):
            if arr[i] == '.' or arr[i] == '':
                continue
            elif stack and arr[i] == '..':
                stack.pop()
            elif not stack and arr[i] == '..':
                continue
         
            else:
                stack.append(arr[i])

        return '/'+'/'.join(stack)