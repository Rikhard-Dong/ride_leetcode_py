from Lib.typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        length = len(A)
        res = [None] * length
        lp, rp = 0, length - 1
        for i in range(0, length):
            num = A[i]
            if num % 2 is 0:
                res[lp] = num
                lp = lp + 1
            else:
                res[rp] = num
                rp = rp - 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))
