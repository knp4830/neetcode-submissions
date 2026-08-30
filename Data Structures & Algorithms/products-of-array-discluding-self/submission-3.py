class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pref, post = [0] * len(nums), [0] * len(nums)

        # Prefix calculation
        for i, n in enumerate(nums):
            if i > 0:
                pref[i] = pref[i - 1] * n
            else:
                pref[i] = n

        # Postfix calculation
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                post[i] = post[i + 1] * nums[i]
            else:
                post[i] = nums[i]

        # result calculation
        for i in range(len(nums)):
            # We want there to be a prefix at -1 and a postfix at + 1
            left = pref[i - 1] if i > 0 else 1
            right = post[i + 1] if i < len(nums) - 1 else 1
            res[i] = left * right
        return res