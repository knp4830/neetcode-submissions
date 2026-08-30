class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rowSet = set()
            colSet = set()
            boxSet = set()

            for j in range(len(board)):
                # Process Row Elements
                if board[i][j] != ".":
                    if board[i][j] in rowSet:
                        return False
                    rowSet.add(board[i][j])
                
                # Process Column Elements
                if board[j][i] != ".":
                    if board[j][i] in colSet:
                        return False
                    colSet.add(board[j][i])

                # Process 3x3 Box Elements
                box_r = 3 * (i // 3) + (j // 3)
                box_c = 3 * (i % 3) + (j % 3)
                box_val = board[box_r][box_c]

                if box_val != ".":
                    if box_val in boxSet:
                        return False
                    boxSet.add(box_val)

        return True
