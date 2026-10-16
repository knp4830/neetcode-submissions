class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Queue Solution
        q = deque()
        res = []

        for R in range(len(nums)):
            while q and nums[q[-1]] < nums[R]: # Smaller ones can never be max
                q.pop()
            q.append(R)

            if q[0] < R - k + 1:    # Front slid out of window
                q.popleft()
            
            if R >= k - 1:      # Window is full
                res.append(nums[q[0]])

        return res 
                


