class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {} # val : index
        # append to hashmap
        # if seen in hashmap, see if nums[i] == nums[j] and j - i <= k
        # if is return true
        # if not seen, append to hashmap
        # end case is there is none, return False

        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            else:
                mp[nums[i]] = i
        return False