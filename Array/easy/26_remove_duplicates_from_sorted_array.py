# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-14 23:03
__author__ = 'f1renze'
__time__ = '2019-02-14 23:03'


"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
"""


def remove_duplicates(nums):
    i = 0
    if not nums:
        return i
    for j in range(1, len(nums)):
        # 将 i 的后一位替换为 j
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == '__main__':
    """
    实际上最后取的是原数组的切片
    """
    n1 = [1, 1, 2]
    n2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(
        n1[:remove_duplicates(n1)],
        n2[:remove_duplicates(n2)]
    )

