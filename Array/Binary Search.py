from typing import List


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         length = len(nums)
#         if length > 1:
#             mid = length // 2
#             if nums[mid] > target:
#                 self.search(nums[:mid], target)
#
#             if nums[mid] < target:
#                 self.search(nums[mid:], target)
#
#             if nums[mid] == target:
#                 return mid
#         else:
#             return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
