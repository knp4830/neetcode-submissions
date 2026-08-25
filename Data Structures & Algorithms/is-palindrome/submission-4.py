class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove the capitals and also lowercase everything
        res = "".join(c.lower() for c in s if c.isalnum())
        #get the front and the end of the string
        x, y = 0, len(res) - 1
        while x <= y:
            if res[x] == res[y]:
                x += 1
                y -= 1
            else:
                return False
        return True