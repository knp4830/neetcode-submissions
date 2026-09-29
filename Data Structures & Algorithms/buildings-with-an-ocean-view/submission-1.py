class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:


        # Tallest is currently the last index
        tallest = heights[-1]
        heights[-1] = len(heights) - 1
        
        # Go through the array backwards starting from the second index
        for i in range(len(heights) - 2, -1, -1):
            # If the height is greater than the tallest
            if heights[i] > tallest:
                # make tallest the height
                tallest = heights[i]
                # update height to index
                heights[i] = i
            # if not we pop it
            else:
                heights.pop(i)

        # we can return and reverse heights now
        return heights