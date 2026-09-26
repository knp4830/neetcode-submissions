class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Two pointer expansion

        res, resLen = "", 0

        # Go through every character in the string considering it the center
        for i in range(len(s)):
            # odd length
            l, r = i, i
            # While its in bounds and a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If its greater than the previous length we update the result and result length
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l: r+1]
                # Then we expand outwards
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1
        
        return res