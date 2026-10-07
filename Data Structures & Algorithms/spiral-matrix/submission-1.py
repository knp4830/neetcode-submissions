class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] # Return list
        top, left, bottom, right = 0, 0, len(matrix), len(matrix[0]) 
        
        # While boundaries have not cross
        while top < bottom and left < right:
            # Top Row (Forward)
            for i in range(left ,right):
                res.append(matrix[top][i])
            top += 1

            # Right Column (Downwards)
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (top < bottom and left < right):
                break

            # Bottom Row (Backwards)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Left Column (Upwards)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res