from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         for j in range(i + 1, len(nums)):
        #             if nums[j] != 0:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 break
        # return nums

        index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
