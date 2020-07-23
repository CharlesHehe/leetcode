# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
#
# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison
# sign flips between each adjacent pair of elements in the subarray.
#
# Return the length of a maximum size turbulent subarray of A.

# Example 1:
#
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = 0
        max_n = 0

        if len(A) == 1 or len(A) == 2 or A.count(A[0]) == len(A):
            return 1
        for i in range(len(A) - 1):
            if i == 0:
                pre = A[i + 1] - A[i]
            elif (A[i + 1] - A[i]) * pre < 0:
                pre = A[i + 1] - A[i]
                if max_n < i + 2 - n:
                    max_n = i + 2 - n
            else:
                pre = A[i + 1] - A[i]
                n = i
                if max_n < i + 2 - n:
                    max_n = i + 2 - n
        return max_n


if __name__ == "__main__":
    s = Solution()
    s.maxTurbulenceSize(

        [4, 8, 12, 16]
    )
