# iterate the String
# Dynamic Programming

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(len(s) - 1, 0):
                if s[i] != s[j]:
                    j - 1
                else:
                    pass

        pass


if __name__ == "__main__":
    a = "dfegrtgtefefe"
    # for i in a:
    #     print(i)
    # print(len(a))
    # print(a[3])
    s = Solution()
    s.longestPalindrome("")
