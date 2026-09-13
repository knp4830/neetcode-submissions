class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Case
        if t == "":
            return ""

        # Initialize two hashmaps
        countT, window = {}, {}
        
        # Fill the first with the amount of values at each character
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Initialize left pointer, have and need variable and result array with a result length
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        # Go through the window with right pointer
        for r in range(len(s)):
            # Update window
            c = s[r]
            window[c] = 1 + window.get(c, 0) 

            # We want to check if this character is in countT and if their values match (amount they appear)
            # If they do we have the correct amount and add it
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # While we have the correct amount of each character
            while have == need:
                # Update our result if it is less than result length
                # This doubles as a max counter cause it must be shorter every time!
                if (r - l + 1) < resLen:
                    # Update the result array and have it as left and right
                    res = [l, r]
                    # Update the size of result length
                    resLen = (r - l + 1)
                # Pop from the left of our window to try to get a smaller answer that still works
                window[s[l]] -= 1
                # If the left was in the count then we need to decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # And we increase l by 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""