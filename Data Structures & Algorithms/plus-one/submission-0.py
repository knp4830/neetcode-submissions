class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Append each digit to a string
        # Turn the string into an integer. Add 1 to it
        # with that integer, each digit we append to a new list
        
        string = ''
        for digit in digits:
            string += str(digit)

        newString = int(string)
        newString += 1
        string = str(newString)
        res = []
        for char in string:
            res.append(int(char))

        return res