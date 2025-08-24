# Last updated: 8/24/2025, 12:31:25 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = (n * (n+1)) // 2
        actualSum = 0

        for i in nums:
            actualSum += i
        
        return expectedSum - actualSum
        