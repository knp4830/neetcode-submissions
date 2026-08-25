class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize our result string and add to it if we get common prefixes
        res = ""

        # We use a double for loop, the first one going through the length of the first string
        # The second going through each element in the array, which s would be "bat", then "bag"
        # then "bank", then "band"
        for i in range(len(strs[0])):
            for s in strs:
                # This if statement checks if the index is current longer than the string its indexing
                # Also checks if the string at the index (current character) 
                # is not equal to the first strings current character which will return the result
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # Otherwise if it is it will append to the result, in this case because it is a string
            # We add to it! not append like to a list
            res += strs[0][i]
        
        return res