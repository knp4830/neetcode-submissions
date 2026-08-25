class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        rp, lp = len(s) - 1, 0
        while lp < rp:
            tmp = s[rp]
            s[rp] = s[lp]
            s[lp] = tmp
            rp -= 1
            lp += 1