class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # We return total at the end of all operations, set it to 0 first
        total = 0
        # We keep a running stack to keep the number
        stack = []
        # We need to iterate through every operation
        for op in operations:
            if op == '+':
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                total += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif op == 'C':
                total -= stack.pop()
            else:
                total += int(op)
                stack.append(int(op))
        return total