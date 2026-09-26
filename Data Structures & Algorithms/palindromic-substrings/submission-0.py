class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        n = len(s)
        # go through every character in teh string considering it the center
        for i in range(n):
            # Even case
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res 