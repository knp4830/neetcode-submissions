class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        count = 0
        for num in hashset:
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                count = max(count, length)

        return count


        #make a set so that there are no repeated
        #We check if there the number has a consecutive number 1 less than it to see if there is a consecutive sequence
        #Iterate through that sequence and continue up until it ends.
        #compare that to the current running total by using max
        #return the result