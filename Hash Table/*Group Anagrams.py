# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
from typing import List
from collections import defaultdict


# dictionary == hashtable key is unique
# sorted()
# Examples of hashable objects:
# int, float, decimal, complex, bool,string, tuple, range, frozenset, bytes
# Examples of Unhashable objects:
# list, dict, set, bytearray, user-defined classes
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


if __name__ == "__main__":
    s = Solution()
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
