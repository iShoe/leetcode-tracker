# Last updated: 8/24/2025, 12:05:51 AM
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # [-1, 0, 3, 5, 9, 12]
        #    0 1 2 3 4 5
        # len = 9 

        start = 0
        end = len(nums) - 1
        mid = 0

        while (start <= end):
            mid = start + ((end - start) // 2)

            if nums[mid] > target:
                end = mid-1
            
            elif nums[mid] < target:
                start = mid+1
            else:
                return mid

            
        return -1