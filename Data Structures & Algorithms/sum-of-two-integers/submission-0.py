class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Python you need masks, this makes it behave like 32-bits
        MASK = 0xFFFFFFFF
        # We use this for positive ints to tell if we have a 32-bit negative
        MAX_INT = 0x7FFFFFFF

        # loop goes until there are no more carry overs
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            
        # If the sign bit is set, convert back to a negative Python int
        # If a <= MAX_INT, the sign bit is 0, so its normal positive
        return a if a <= MAX_INT else ~(a ^ MASK)