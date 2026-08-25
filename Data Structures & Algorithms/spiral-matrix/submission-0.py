class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        if not matrix: #base case, there isn't a matrix
            return res
        
        #initialize the corners, we set top and left equal to 0 because our starting point is in the top left corner
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0

        while top <= bottom and left <= right: #here we keep spiraling inwards
            #traverse the top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1 #shrink the top boundary, we are not subtracting because the next input in the array going lower is going up by 1
            #traverse right column and down
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            # Traverse bottom row (if its not already passed)
            if top <= bottom:
                for i in range(right, left - 1, -1): # we are going backwards here
                    res.append(matrix[bottom][i])
                bottom -= 1
            # Traverse left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            
        return res

