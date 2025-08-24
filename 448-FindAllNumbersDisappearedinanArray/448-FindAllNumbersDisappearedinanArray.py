# Last updated: 8/24/2025, 12:51:41 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # hset = set(nums)
        # result = []

        # for i in range(1, len(nums)+1):
        #     if i not in hset:
        #         result.append(i)
        
        # return result

        # No extra space solution

        result = []

        for i in range(len(nums)):
            n = abs(nums[i])
            index = n - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        for i in range(len(nums)):
            if(nums[i] > 0):
                result.append(i+1)

        return result
        