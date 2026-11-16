class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Using Binary Search we take the min rate and max rate (which is 1 b/hr and biggest pile b/hr)
        l, r = 1, max(piles)
        res = r # total max

        while l <= r:
            k = (l + r) // 2        # Rate at which we eat (and we will be trying)

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)           # We round up here to finish the piles by the hour

            # This case that means theres still time left, so we can eat less bananas
            if totalTime <= h:
                res = k
                r = k - 1
            # This means we didn't finish the bananas fast enough
            else:
                l = k + 1
        return res