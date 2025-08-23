# Last updated: 8/23/2025, 3:57:59 AM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while (i >= 0 and j >= 0):
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # Copy remaining elements from nums2 array, if any.
        # We do not need to do the same for nums1 
        # because they are already in position in nums1 
        # (Where they would have to be copied into)
        while (j >= 0):
            nums1[k] = nums2[j]
            j -= 1
            k -= 1 




        