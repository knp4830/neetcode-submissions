class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l, visit = 0, 0, set() # keeps track of longest substring, left side of window, duplicates

        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
            res = max(res, (r - l) + 1)
        
        return res