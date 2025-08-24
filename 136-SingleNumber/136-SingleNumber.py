# Last updated: 8/24/2025, 12:40:27 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        
        return result