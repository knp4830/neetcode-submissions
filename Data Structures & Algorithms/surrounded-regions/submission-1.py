class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Review
        row, col = len(board), len(board[0])

        # DFS helper function
        def transform(r, c):
            if (r < 0 or c < 0 or r == row or c == col or board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            transform(r + 1, c)
            transform(r - 1, c)
            transform(r, c + 1)
            transform(r, c - 1)

        # Transform any not enclosed O -> T
        for r in range(row):
            for c in range(col):
                if (board[r][c] == "O" and r in [0, row - 1] or c in [0, col - 1]):
                    transform(r,c)

        # Transform any Enclosed O -> X
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Transform them Back T -> O
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"