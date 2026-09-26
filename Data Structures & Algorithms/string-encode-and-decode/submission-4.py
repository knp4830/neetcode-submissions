class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        # Go through length of string
        while i < len(s):
            j = i
            # While we are still looking for the digits increase j
            while s[j] != "#":
                j += 1
            # Once we have reached #, we know the length of of the string now
            length = int(s[i:j])

            # We append from after the # to the length
            res.append(s[j + 1: j + 1 + length])
            # Increment our i
            i = j + 1 + length
        
        return res
