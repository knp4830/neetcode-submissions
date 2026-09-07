class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Get the cars in reverse order
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        stack = []
        # Reverse the pair 
        pair.sort(reverse=True)
        # go through the pair and its speed
        for p, s in pair:
            # Start appending to the time to destination of each car
            stack.append((target - p) / s)
            # if the stack greater than or at 2 and the top of the stack (car)
            # takes less time than the car in front of it. We can pop it
            # meaning its in the same fleet (so we don't need to recount)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
