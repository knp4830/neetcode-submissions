class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        least = 1
        most = max(piles)
        res = most

        while least <= most:
            middle = least + (most - least) // 2

            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / middle)
            
            if time <= h:
                res = middle
                most = middle - 1
            else:
                least = middle + 1
        
        return res 