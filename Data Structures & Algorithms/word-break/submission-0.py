class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # cache
        dp = [False] * (len(s) + 1)
        # Base case
        dp[len(s)] = True
        # Go from the back of the string
        for i in range(len(s) - 1, -1, -1):
            # Try every word in our word dict
            for w in wordDict:
                # If its within the length of the word and the word is the same
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]

