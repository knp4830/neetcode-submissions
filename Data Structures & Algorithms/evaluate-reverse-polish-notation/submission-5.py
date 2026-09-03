class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Lambda operation
        ops = {
            "+": lambda b, a: b + a,
            "-": lambda b, a: b - a,
            "*": lambda b, a: b * a,
            "/": lambda b, a: int(b / a),
        }
        stack = []
        for c in tokens:
            if c in ops:
                a, b = stack.pop(), stack.pop()
                stack.append(ops[c](b, a))
            else:
                stack.append(int(c))
        return stack[0]