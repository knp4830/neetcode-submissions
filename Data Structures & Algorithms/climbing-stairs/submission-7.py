class Solution:
    def climbStairs(self, n: int) -> int:
        # Review and DP space optimized
        one, two = 1, 1 # one way to get either

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one