# Last updated: 8/23/2025, 3:27:32 AM
class Solution:

    def reverse_array(self, nums: List[int], start: int, end: int) -> None:
        i = start
        j = end - 1

        while (i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        # reverse entire array
        self.reverse_array(nums, 0, n)
        
        # reverse first k element
        self.reverse_array(nums, 0, k)
        # reverse rest
        self.reverse_array(nums, k, n)



        # Uses extra space O(n)
        # n = len(nums)
        # rotate = k % n

        # result = nums[-rotate:] + nums[:n-rotate]
        # for i in range(len(nums)):
        #     nums[i] = result[i]