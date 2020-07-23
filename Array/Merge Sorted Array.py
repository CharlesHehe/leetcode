# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         nums1[0:m]+nums2[0:n]
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] =nums2[0:n]
        nums1.sort()
        print(nums1)
        # nums1[m:] = nums2[:]
        # nums1.sort()
        # print(nums1)


if __name__ == "__main__":
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)