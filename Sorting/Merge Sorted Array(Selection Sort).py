from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]

        for i in range(len(nums1)):
            min_index = i
            for j in range(i, len(nums1)):
                if nums1[j] < nums1[min_index]:
                    min_index = j

            nums1[i], nums1[min_index] = nums1[min_index], nums1[i]

        print(nums1)


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
