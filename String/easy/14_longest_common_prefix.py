# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-12 22:34
__author__ = 'f1renze'
__time__ = '2019-02-12 22:34'


"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


def solution(strs):
    """
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Longest Common Prefix.
    Memory Usage: 10.9 MB, less than 0.92% of Python online submissions for Longest Common Prefix.
    :param strs:
    :return:
    """
    if not strs:
        return ''
    strs = sorted(strs, key=len)
    r = list()
    tmp = None

    for n in range(len(strs[0])):
        for i, s in enumerate(strs):
            if i == 0:
                tmp = s[n]
            elif tmp != s[n]:
                return ''.join(r)
        r.append(tmp)
    return ''.join(r)


if __name__ == '__main__':
    pass
