
import heapq
import collections
from typing import List


"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution:
    @staticmethod
    def top_k_frequent(nums: List[int], k: int) -> List[int]:
        mapper = dict()
        for i in set(nums):
            mapper[i] = nums.count(i)

        n_largest = heapq.nlargest(k, list(mapper.items()), key=lambda x: x[1])
        return [x[0] for x in n_largest]


class Solution2:
    @staticmethod
    def top_k_frequent(nums: List[int], k: int) -> List[int]:
        return sorted(set(nums), key=lambda x: nums.count(x))[::-1][:k]


class Solution3:
    @staticmethod
    def top_k_frequent(nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        res = dic.most_common(k)
        return [ele[0] for ele in res]
