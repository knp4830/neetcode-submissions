class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # We return total at the end of all operations, set it to 0 first
        total = 0
        # We keep a running stack to keep the number
        stack = []
        # We need to iterate through every operation
        for op in operations:
            if op == '+':
                val = stack[-1] + stack[-2]
            elif op == 'D':
                val = 2 * stack[-1]
            elif op == 'C':
                total -= stack.pop()
                continue
            else:
                val = int(op)
            total += val
            stack.append(val)
        return total