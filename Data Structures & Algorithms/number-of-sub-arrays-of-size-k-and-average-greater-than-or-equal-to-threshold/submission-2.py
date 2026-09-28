class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subArray = deque()
        res = 0 # Result counter
        L = 0 # Left pointer

        # Slide the window
        for R in range(len(arr)):
            # If it is greater than k remove the leftmost element
            if R - L + 1 > k:
                subArray.popleft()
                L += 1
            # Append the right element
            subArray.append(arr[R])
            # Get the total
            total = int(sum(subArray) / k)
            # Check if the total is >= and of size k and add to result
            if len(subArray) == k and total >= threshold:
                res += 1
            
        return res