class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Use sliding window fixed size approach, keep an array, if size array is greater
        # size k, remove L add R. Then check if it is valid, make sure that the averages turn
        # into integers to be able to compare. If it is add to the result and continue


        subArray = deque()
        res = 0 # Result counter
        L = 0 # Left pointer

        for R in range(len(arr)):
            if R - L + 1 > k:
                subArray.popleft()
                L += 1
            subArray.append(arr[R])
            total = int(sum(subArray) / k)
            if len(subArray) == k and total >= threshold:
                res += 1
            
        return res