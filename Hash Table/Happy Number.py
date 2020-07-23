# sum(int(digit) ** 2 for digit in str(n))

class Solution:
    def isHappy(self, n: int) -> bool:
        count = 10
        while n != 1 and count > 0:
            count -= 1

            n = sum(int(digit) ** 2 for digit in str(n))
            # for i in str(n):
            #     cur_sum += int(i) ** 2

            # cur_sum = 0
        if count == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    Solution().isHappy(19)