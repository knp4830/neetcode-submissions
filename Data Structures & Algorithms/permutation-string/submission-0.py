class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case
        if len(s1) > len(s2):
            return False
        
        # Can be done in array or hashmap
        s1Count, s2Count = [0] * 26, [0] * 26

        # Go through every character in str1 and get its key
        # Get s2's current window as well since its same length as s1
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # Get ascii value
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        # Get the number of matches
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Sliding window portion
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: # If they do match we can immediately return true
                return True
            index = ord(s2[r]) - ord('a') # We have to map the new character to an index
            s2Count[index] += 1 # We add that to the index
            if s1Count[index] == s2Count[index]: # If it matches a character in the first string
                matches += 1 #increment the count
            elif s1Count[index] + 1 == s2Count[index]: # We know its wrong though if its +1 is equal cause it would be too much
                matches -= 1 # so we would have to decrement
                
            index = ord(s2[l]) - ord('a') # Do the same for when we subtract a character from the left
            s2Count[index] -= 1 # we remove the character at left index
            if s1Count[index] == s2Count[index]: # Check if the counts are equal after decrementing
                matches += 1 # Increase if they are
            elif s1Count[index] - 1 == s2Count[index]: #Check fi by decrementing it is less by 1
                matches -= 1 # we have to unmatch
            l += 1 # increase the left slider

        return matches == 26 # Check and return if matches are equal to 26
