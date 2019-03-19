
import math
import heapq
from typing import List


class Solution:

    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # mapper list, some distance may be repeat
        mapper = [[self.eculidean_distance(*i), i] for i in points]

        # build a minimum heap
        distances = [x[0] for x in mapper]
        heapq.heapify(distances)
        targets = heapq.nsmallest(k, distances)

        return [i[1] for i in mapper if i[0] in targets]

    @staticmethod
    def eculidean_distance(x, y):
        return math.sqrt(x ** 2 + y ** 2)


class Solution2:
    @staticmethod
    def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: (x[0]*x[0] + x[1]*x[1]))[:k]


def t1():
    return Solution().k_closest([[0, 1], [1, 0]], 2)


if __name__ == '__main__':
    print(
        t1()
    )
