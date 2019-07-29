import math


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        flag = x >= 0
        res = 0
        x = abs(x)
        while x is not 0:
            res = res * 10 + x % 10
            x = x // 10
        if not flag:
            res = res * -1
        if res > 2147483648 or res < -2147483648:
            return 0
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
