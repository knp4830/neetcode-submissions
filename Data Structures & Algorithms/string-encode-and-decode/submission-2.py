class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # up to j but not including
            length = int(s[i:j])
            # first character in the string itself, to 
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
