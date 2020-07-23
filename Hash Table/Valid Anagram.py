# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict()
        d[tuple(sorted(s))] = s
        d[tuple(sorted(t))] = t
        if len(d) == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    Solution().isAnagram("anagram", "nagaram")