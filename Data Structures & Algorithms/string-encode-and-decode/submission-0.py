class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = []
        for i in strs:
            encoded_piece = str(len(i)) + "#" + i
            sentence.append(encoded_piece)
        return ''.join(sentence)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 #pointer to scan through the string
        while i < len(s):
            j = i #read the number until we hit '#'
            while s[j] != '#': #we do this because before every word, we have a number
                j += 1 #if it is not we continue to increment until we hit another number
            length = int(s[i:j]) # s[i:j] is the number (as a string), convert it into an integer

            word = s[j+1 : j+1+length] #this takes us from after the '#' until the next number because of the j+1+length # plus word
            result.append(word)

            i = j + 1 + length # we move the pointer to the start of the next encoded chunk

        return result
