class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # check if its alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            # if they're not equal we want to return false immediately
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True