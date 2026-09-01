class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0 # Allows us to be more efficient by keeping the max frequency
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # Checks whether the old maxfrequency or adding the new character is greater
            # While the window is not valid, check if the number of replacements needed is greater than allowed
            # which is k number of replacements allowed
            while (r - l + 1) - maxf > k:
                # Decrement the count at the left by 1 because we are increasing it
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1) # Max of result and size of window (r - l + 1)
        return res