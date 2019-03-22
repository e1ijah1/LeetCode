from typing import List
from functools import reduce


class Solution:
    @staticmethod
    def kth_smallest(matrix: List[List[int]], k: int) -> int:
        re = reduce(lambda x, y: x + y, matrix)
        return sorted(re)[k - 1]
