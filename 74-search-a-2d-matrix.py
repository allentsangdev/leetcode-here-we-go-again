from typing import List


class Solution:
    def bSearch(self, nums: List[int], target: int) -> bool:
        L, R = 0, len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            if nums[M] == target:
                return True
            if nums[M] > target:
                R = M - 1
            if nums[M] < target:
                L = M + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mRow = (top + bot) // 2
            if matrix[mRow][-1] == target:
                return True
            elif target > matrix[mRow][-1]:
                top = mRow + 1
            elif target < matrix[mRow][0]:
                bot = mRow - 1
            else:
                return self.bSearch(matrix[mRow], target)

        return False
