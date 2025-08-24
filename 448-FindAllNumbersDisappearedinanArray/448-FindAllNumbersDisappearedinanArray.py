# Last updated: 8/24/2025, 12:42:58 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hset = set(nums)
        result = []

        for i in range(1, len(nums)+1):
            if i not in hset:
                result.append(i)
        
        return result

        