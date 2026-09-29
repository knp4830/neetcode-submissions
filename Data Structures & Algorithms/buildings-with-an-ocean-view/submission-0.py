class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Stack is initialized with the last index and we use that to determine next
        stack = [len(heights) - 1]

        # Starting from second to last element going backwards to first
        for i in range (len(heights) - 2, -1, -1):
            # If the height at that index is greater than the top of our stack
            if heights[i] > heights[stack[-1]]:
                stack.append(i)


        return stack[::-1]
