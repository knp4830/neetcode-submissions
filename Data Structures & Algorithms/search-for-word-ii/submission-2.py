# Tree class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create our root and for every word we add it to our Trie
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        # Result is the set of words so we dont want to return duplicates, 
        # Visit makes sure we don't visit duplicates 
        res, visit = set(), set()

        # row, col, current node we're at in our Trie, and what is the word so far
        # DFS function
        def dfs(r, c, node, word):
            # If row or column not in bounds or the node has been visited or its not even in the Trie
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or 
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            # If it does pass, then we know its valid
            visit.add((r,c))
            node = node.children[board[r][c]] # node exists
            word += board[r][c]
            # Checks if its the end of a word we add it
            if node.isWord:
                res.add(word)

            # Recursive case, check every side with the current node and word we have built
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)


            # Once we're done visiting we remove it
            visit.remove((r,c))

        # Go through every single starting position
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
                    
        return list(res)