class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Review with set
        sub = set() # keeps track of characters
        L = 0 # Left pointer
        res = 0 # result initialized

        # Iterate through the string
        for R in range(len(s)):
            while s[R] in sub:
                sub.remove(s[L])
                L += 1
            sub.add(s[R])
            res = max(res, R - L + 1)

        return res