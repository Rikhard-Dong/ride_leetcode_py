"""
思路:
把每次计算结果放入到一个set, 如果某次的计算结果已经在set中了, 则说明不是快乐数, 不然最后计算结果肯定会变成1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        if n is 0:
            return False
        basket = set()
        while n != 1:
            n = self.cal(n)
            if n in basket:
                return False
            basket.add(n)
        return True

    # 计算每位平方之后和
    def cal(self, n):
        res = 0
        while n is not 0:
            res = res + (n % 10) ** 2
            n = n // 10
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2))
    print(s.isHappy(3))
    print(s.isHappy(4))
    print(s.isHappy(5))
    print(s.isHappy(6))
    print(s.isHappy(7))
