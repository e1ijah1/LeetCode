
from typing import List

"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""


class Solution:
    def sorted_squares(self, a: List[int]) -> List[int]:
        """
        双指针解法
        :param a:
        :return:
        """
        if not a:
            return a

        result = [0 for _ in range(len(a))]

        head, tail = 0, len(a) - 1
        r_ptr = len(result) - 1

        while head <= tail:
            if abs(a[head]) < abs(a[tail]):
                result[r_ptr] = a[tail] ** 2
                tail -= 1
            else:
                result[r_ptr] = a[head] ** 2
                head += 1

            r_ptr -= 1

        return result
