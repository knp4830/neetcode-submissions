class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        
        if total % 2 == 1: # odd length
            mid = total // 2
        else:
            mid = total // 2 - 1
            mid2 = total // 2

        i = 0 # for nums1
        j = 0 # for nums 2
        while i < len(nums1) and j < len(nums2) and i+j <= mid:
            if nums1[i] <= nums2[j]:
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1
        
        while i < len(nums1) and i+j <= mid:
            current = nums1[i]
            i += 1
        
        while j < len(nums2) and i+j <= mid:
            current = nums2[j]
            j += 1

        if total % 2 == 1:
            return current
        else:
            # pick next value safely
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                var = nums1[i]
            else:
                var = nums2[j]
            return (current + var) / 2
