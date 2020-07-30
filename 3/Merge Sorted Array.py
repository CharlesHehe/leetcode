# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[m:] = nums2[:n]

    for i in range(len(nums1)):
        min_index = i
        for j in range(i, len(nums1)):
            if nums1[min_index] > nums1[j]:
                min_index = j

        nums1[i], nums1[min_index] = nums1[min_index], nums1[i]
    return nums1


class Solution:
    print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
