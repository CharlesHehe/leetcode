from typing import List


class Solution:
    max_length = 0

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > self.max_length:
            self.max_length = len(nums)
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]

            self.sortArray(L)
            self.sortArray(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
        if len(nums) == self.max_length:
            return nums


Solution().sortArray([38, 43, 20, 3, 9, 82, 10])
