class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort O(n log n) time and O(n) space
        listS = sorted(s)
        listT = sorted(t)
        if len(listT) != len(listS):
            return False
        for i in range(len(s)):
            if listS[i] != listT[i]:
                return False
        return True