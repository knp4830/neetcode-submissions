class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Review
        n = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # Loop through the entire board
        for row in range(n):
            for col in range(n):
                # Get the value at current index
                val = board[row][col]
                if val == '.':
                    continue
                
                # Get the box index (This separates the boxes 0-8)
                box_index = (row // 3) * 3 + (col // 3)
                if (val in rows[row] or val in cols[col] or val in boxes[box_index]):
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                boxes[box_index].add(val)
        return True 