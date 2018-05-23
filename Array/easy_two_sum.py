# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-23 上午11:59
__author__ = 'f1renze'
__time__ = '18-5-23 上午11:59'



'''
Two Sum

example:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for index, item in enumerate(nums):
            result = target - item
            if result in tmp:
                return [tmp[result], index]
            else:
                tmp[item] = index

if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 7, 11, 15]
    print(s.twoSum(l, 9))