class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = sorted(s)
        listT = sorted(t)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if listS[i] == listT[i]:
                continue
            else:
                return False
        return True