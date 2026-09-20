class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0]) # Get size of board
        path = set() # Hashset keeps track of visited characters

        def dfs(r, c, i): # row, col, current character within target word
            if i == len(word):
                return True

            # If row or col are out of bounds, or the character we are looking for is not in board, or
            # the character has already been visited
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return
            # If it passes the case then it must be valid so we add it to the set
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            # Clean up, we're no longer visiting that position inside of our path
            path.remove((r, c))
            return res

        # Brute force: checking every position in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False