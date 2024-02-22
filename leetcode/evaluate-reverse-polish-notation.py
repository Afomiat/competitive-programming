class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # val = 0
        for i in tokens:
        
                if i == "+":
                    a = stack.pop()
                    b = stack.pop()
                    val =(b+a)
                    stack.append(val)
                elif i == "-":
                    a = stack.pop()
                    b = stack.pop()
                    val =(b-a)
                    stack.append(val)
                elif i == "*":
                    a = stack.pop()
                    b = stack.pop()
                    val =(b*a)
                    stack.append(val)
                elif i == "/":
                    a = stack.pop()
                    b = stack.pop()
                    val =int(b/a)
                    stack.append(val)
                else:
                    stack.append(int(i))
        return stack[0]

