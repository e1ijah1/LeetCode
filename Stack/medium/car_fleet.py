# -*- coding: utf-8 -*-
# Created by f1renze on 2018/11/21 下午11:27

import unittest

''' 853
N  辆车沿着一条车道驶向位于 target 英里之外的共同目的地。

每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。

一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。

此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。

车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。

即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。

 

会有多少车队到达目的地?

 

示例：

输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
输出：3
解释：
从 10 和 8 开始的车会组成一个车队，它们在 12 处相遇。
从 0 处开始的车无法追上其它车，所以它自己就是一个车队。
从 5 和 3 开始的车会组成一个车队，它们在 6 处相遇。
请注意，在到达目的地之前没有其它车会遇到这些车队，所以答案是 3。
'''


class Solution(object):

    @staticmethod
    def car_fleet(target, position, speed):
        """
        题目重点在于2车途中相遇即认为是一个车队,
        若最后在终点相遇也认为是一个车队(包括所有车在终点相遇的情况)
        :param target:
        :param position:
        :param speed:
        :return:
        """
        # sorted 之后会按 position 由小到大排序
        cars = sorted(zip(position, speed))
        print(cars)
        times = [float(target - p) / s for p, s in cars]
        print(times)
        count = 0
        while len(times) > 1:
            # 距离最近的先出栈
            cur = times.pop()
            # 若后一位比前一位速度大(居后者距离远), 认为合并为车队, 总数 + 1
            if cur < times[-1]:
                count += 1
            # 否则比较后后一位的速度若比当前的 cur 速度大, 会与它前一位合并
            else:
                times[-1] = cur
        # 若无超车情况视为所有车在终点相遇, bool(times) == 1
        # count + True == count + 1 (False == 0)
        return count + bool(times)


class Tester(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.target = [
            12,
            10
        ]
        self.position = [
            [10, 8, 0, 5, 3],
            [2, 4]
        ]
        self.speed = [
            [2, 4, 1, 1, 3],
            [3, 2]
        ]

    def test_logic(self):
        result = self.solution.car_fleet(self.target[0],
                                         self.position[0],
                                         self.speed[0])
        r2 = self.solution.car_fleet(self.target[1],
                                     self.position[1],
                                     self.speed[1])
        self.assertEqual(result, 3)
        self.assertEqual(r2, 1)


if __name__ == '__main__':
    unittest.main()
