class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We want to store everything in a max heap
        # from there we take the heaviest stop and pop it
        # Pop the next stone since it should be the heaviest now
        # check if they are same weight which means both get destroyed
        # If the heaviest is heavier slightly we do y - x
        # place it back into the heap
        # keep going until there is one left
        # or return 0 if none remain

        # Get the negative value for the array
        # Once this turns into a heap we can get the positive
        arr = [-s for s in stones]
        # Turn the array into a heap, now the largest number is at the top
        heapq.heapify(arr)
        while len(arr) > 1:
            largest = -heapq.heappop(arr)
            largest2 = -heapq.heappop(arr)
            if largest == largest2:
                continue
            else:
                heapq.heappush(arr, -(largest - largest2))
            
        return -(arr[0]) if len(arr) >= 1 else 0



