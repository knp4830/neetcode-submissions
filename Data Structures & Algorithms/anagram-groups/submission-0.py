from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for i in strs:
            sorted_i = tuple(sorted(i)) #we change into a tuple because it is an immutable datatype which allows it to be stored as a key
            anagram_map[sorted_i].append(i)
        
        for value in anagram_map.values():
            result.append(value)
        
        return result