class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            diff = abs(nums[i] - target)
            if diff in hashMap:
                return [i, hashMap[diff]]
            else:
                hashMap[nums[i]] = i
