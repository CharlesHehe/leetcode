from typing import List


# Quick Sort
class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        target_index = len(nums) - k
        while low <= high:
            pi = self.partition(nums, low, high)
            if pi > target_index:
                high = pi - 1
            elif pi < target_index:
                low = pi + 1
            else:
                return nums[pi]


Solution().findKthLargest([3, 2, 1, 5, 6, 7, 8, 3, 4, 4], 2)
