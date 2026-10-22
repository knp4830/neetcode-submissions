class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Base Case
        if sum(gas) < sum(cost):
            return -1

        total = 0                   # Tracks the gas balance (if it becomes < 0 then we reset to 0).
        res = 0                     # Index of current result set at first station
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res