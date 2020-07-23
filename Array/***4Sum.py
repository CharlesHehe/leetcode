from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out_list = []
        in_list = []
        a = nums
        for i, q in enumerate(a):
            b=a
            b.pop(i)
            for j, w in enumerate(b):
                c=b
                c.pop(j)
                for m, e in enumerate(c):
                    d=c
                    d.pop(m)
                    for n, r in enumerate(d):
                        if q + w + e + r == target:
                            in_list.append(q)
                            in_list.append(w)
                            in_list.append(e)
                            in_list.append(r)
                            out_list.append(in_list)
        return out_list


Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
