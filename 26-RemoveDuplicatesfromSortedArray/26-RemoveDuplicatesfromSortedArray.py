# Last updated: 8/23/2025, 3:27:06 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  # First element is always unique
        
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:  # Different from previous unique element
                nums[k] = nums[i]
                k += 1
        
        return k