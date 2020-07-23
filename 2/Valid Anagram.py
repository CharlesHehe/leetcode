from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        dict_s[tuple(sorted(s))] = s
        dict_s[tuple(sorted(t))] = t
        if len(dict_s) == 1:
            return True
        else:
            return False
