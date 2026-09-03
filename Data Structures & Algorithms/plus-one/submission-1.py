class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the back of the list
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9 we can add normally
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise we have to turn it into 0 and add it to the next one
            digits[i] = 0
        
        # The last case would mean every digit after the first is 9, ex. 999 -> 1000
        return [1] + digits