# Input: s = "anagram", t = "nagaram"
# Output: true


from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        d[tuple(sorted(s))] = s
        d[tuple(sorted(t))] = t
        if len(d) == 1:
            return True
        else:
            return False


Solution().isAnagram("anagram", "nagaram")
