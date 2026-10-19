class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Review DP
        # Helper Function
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""
        for i in range(len(s)):
            odd = expand(i, i)                 # Odd
            even = expand(i, i + 1)            # Even
            res = max(res, odd, even, key=len) # keep longest string

        return res
    