class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
            
                if val == '.':
                    continue

                box_index = (row // 3) * 3 + (col // 3)
                # check each column, row and box at the same time for duplicates
                if (val in rows[row] or val in cols[col] or val in boxes[box_index]):
                    return False
                
                # Otherwise we add them to the set
                rows[row].add(val)
                cols[col].add(val)
                boxes[box_index].add(val)
        
        return True