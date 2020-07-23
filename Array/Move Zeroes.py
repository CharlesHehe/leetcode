from typing import List


class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        n = nums.count(0)
        nums.sort()
        nums = nums[n:]
        while n > 0:
            nums.append(0)
            n -= 1
        print(nums)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[index] = num
                index += 1

        for i in range(index, len(nums)):
            nums[i] = 0
        print(nums)


if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0, 1, 0, 3, 12])