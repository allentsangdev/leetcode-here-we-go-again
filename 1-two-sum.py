from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hMap:
                return [i, hMap[diff]]
            else:
                hMap[nums[i]] = i
