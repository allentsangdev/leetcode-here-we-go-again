import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        numberOfPiles = len(piles)
        if numberOfPiles == h:
            return max(piles)

        L, R = 1, max(piles)
        result = R

        while L <= R:
            m = (L + R) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / m)

            if hours <= h:

                result = min(result, m)
                R = m - 1
            elif hours > h:
                L = m + 1

        return result
