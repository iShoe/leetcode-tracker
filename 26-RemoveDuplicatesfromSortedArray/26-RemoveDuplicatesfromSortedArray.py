# Last updated: 8/23/2025, 4:06:36 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # write pointer, start from index 1 (2nd lement) because 
        # first element is always unique
        k = 1  
        
        for i in range(1, len(nums)):
            # Different from previous unique element
            if nums[i] != nums[k-1]:  
                nums[k] = nums[i]
                k += 1
        
        return k