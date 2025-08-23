# Last updated: 8/23/2025, 3:27:19 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's voting algorithm
        # Space: O(1)
        mele = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                mele = nums[i]

            if nums[i] == mele:
                count += 1
            else:
                count -= 1

        return mele

        # Uses O(n) space for hashmap
        # mele = 0
        # count = 0
        # hmap = {}

        # for i in range(len(nums)):
        #     hmap[nums[i]] = hmap.get(nums[i], 0) + 1
        #     if (hmap[nums[i]] > count):
        #         mele = nums[i]
        #         count = hmap[nums[i]]
            
        # return mele


        

        