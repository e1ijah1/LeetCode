# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-23 下午12:01
__author__ = 'f1renze'
__time__ = '18-5-23 下午12:01'

'''
Group Anagrams medium

example:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''


class Solution(object):
    @classmethod
    def group_anagrams(cls, str_list):
        """
        :type str_list: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for str_ in str_list:
            d.setdefault(''.join(sorted(str_)), []).append(s)

        return list(d.values())


if __name__ == '__main__':
    s = Solution()
    l1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    l2 = ["cab", "pug", "pei", "nay", "ron",
          "rae", "ems", "ida", "mes"]
    l3 = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(s.group_anagrams(l1),
          s.group_anagrams(l2),
          s.group_anagrams(l3),
          sep='\n\n')
