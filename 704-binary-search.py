from typing import List


def binary_search(nums: List[int], target: int) -> int:
    L, R = 0, len(nums) - 1
    while L <= R:
        M = (L + R) // 2

        if nums[M] == target:
            return M
        elif nums[M] > target:
            R = M - 1
        else:
            L = M + 1
    return -1


# Test cases
testList1 = [1, 2, 3, 4, 5, 6]
target1 = 5
result1 = binary_search(testList1, target1)
print(result1)
assert result1 == 4

testList2 = [4, 7, 9, 10, 99, 100]
target2 = 100
result2 = binary_search(testList2, target2)
print(result2)
assert result2 == 5

testList3 = [1, 2, 3, 4, 5, 6]
target3 = 100
result3 = binary_search(testList3, target3)
print(result3)
assert result3 == -1
