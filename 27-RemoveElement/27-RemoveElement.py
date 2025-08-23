# Last updated: 8/23/2025, 4:13:13 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k - write pointer, it will stop at invalid positions.
        # invalid = element "val" (which has to be removed)
        # Then later the element gets overwritten thats why its writer pointer
        k = 0
        n = len(nums)

        for i in range(n): # i - read pointer
            if (nums[i] != val):
                nums[k] = nums[i] # copy valid element
                k += 1
        
        return k
            