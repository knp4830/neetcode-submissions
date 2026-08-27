class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap that takes lists as keys and also
        # default dict allows new keys to be appended
        res = defaultdict(list)
        # Check each character in string
        for string in strs:
            # We sort each string but because it returns a list
            # we need to join them back together
            sortedS = ''.join(sorted(string))
            # for the key we append the string
            # ex: sortedS is "aet" and we have string "eat" it appends
            # "eat" to the value
            res[sortedS].append(string)
        
        # we return the list of values
        return list(res.values())