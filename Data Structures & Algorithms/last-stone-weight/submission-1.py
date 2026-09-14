class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Get the negative value for the array
        # Once this turns into a heap we can get the positive
        arr = [-s for s in stones]
        # Turn the negative array into a heap, now the largest number is at the top
        heapq.heapify(arr)

        # While there is still something in the array
        while len(arr) > 1:
            # Pop from the heap
            largest, largest2 = -heapq.heappop(arr), -heapq.heappop(arr)
            # If they weigh the same, it means both are destroyed (we don't add back)
            if largest == largest2:
                continue
            # Else: largest - second largest because second cant be greater than first in heap
            else:
                heapq.heappush(arr, -(largest - largest2))
            
        # Return the top if there is something in the array else 0
        return -(arr[0]) if len(arr) >= 1 else 0



