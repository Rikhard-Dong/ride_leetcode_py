from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k is not 0:
            for _ in range(k):
                nums.insert(0, nums.pop())


if __name__ == '__main__':
    s = Solution()
    num: List[int] = [1, 2, 3, 4]
    s.rotate(num, 5)
    print(num)
