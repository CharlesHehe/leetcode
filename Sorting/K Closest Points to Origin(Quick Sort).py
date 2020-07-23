from typing import List
from collections import defaultdict


class Solution:
    d = defaultdict(int)

    def partition(self, points, low, high):
        pivot = points[high][0] ** 2 + points[high][1] ** 2
        i = low - 1
        for j in range(low, high):
            cur = points[j][0] ** 2 + points[j][1] ** 2
            self.d[cur] += 1
            if cur <= pivot:
                i += 1
                points[i], points[j] = points[j], points[i]

        points[i + 1], points[high] = points[high], points[i + 1]
        return i + 1

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        low = 0
        high = len(points) - 1

        while low <= high:
            pi = self.partition(points, low, high)
            if pi > K:
                high = pi - 1
            elif pi < K:
                low = pi + 1
            else:
                return points[:K]


Solution().kClosest([[0, 1], [1, 0]], 2)
