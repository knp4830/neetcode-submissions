class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        sub = set()

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            res = max(res, r - l + 1 )

        return res
