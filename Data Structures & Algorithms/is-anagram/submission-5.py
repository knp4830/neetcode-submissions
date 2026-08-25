class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base case 
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)