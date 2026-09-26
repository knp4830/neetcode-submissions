class Solution:
    def numDecodings(self, s: str) -> int:
        # Number of characters
        n = len(s)
        
        # dp[i] = ways to decode the first i characters of s
        # we use n + 1 because dp[0] is the empty prefix
        dp = [0] * (n + 1)
        # Seed: one way to decode nothing, lets the first single digit count as one decode
        dp[0] = 1

        # build up from 1 to all n characters
        for i in range(1, n + 1):
            # Option 1: decode the last character alone
            # s[i - 1] is the i-th character shifted by 1
            # '0' cant stand alone, so only 1-9 count
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Option 2: decode the last two characters as a pair
            # we need at least 2 characters i >= 2
            # we need s[i - 2:i] is the last two characters; valid if 10-26
            # (This also rejects "0x" pairs like 06 since int ("06") = 6)
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                # Every decoding of the first i-2 chars
                # plus this pair is a valid decoding
                dp[i] += dp[i - 2]
        # dp[n] covers the whole string 
        return dp[n]