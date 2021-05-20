class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                stack[-2] = str(int(eval(stack[-2] + token +stack[-1])))
                stack.pop()
            else:
                stack.append(token)
        return stack[-1]
