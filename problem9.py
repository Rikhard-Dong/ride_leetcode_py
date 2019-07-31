class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        n = 0
        temp = x
        while x != 0:
            n = n * 10 + (x % 10)
            x = x // 10
        return temp == n


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(123))
    print(s.isPalindrome(121))
