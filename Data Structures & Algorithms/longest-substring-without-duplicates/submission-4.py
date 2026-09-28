class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Review with hashmap
        hmap = {} # Hmap
        res = 0 # length result variable
        L = 0 # Left pointer

        # Go through string
        for R in range(len(s)):
            # If the character is in hmap
            if s[R] in hmap:
                # Move L to where it last appeared + 1
                L = max(hmap[s[R]] + 1, L)
            
            # 
            hmap[s[R]] = R
            res = max(res, R - L + 1)

        return res