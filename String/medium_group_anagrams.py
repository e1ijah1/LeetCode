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
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            d.setdefault(''.join(sorted(s)), []).append(s)

        return list(d.values())

if __name__ == '__main__':
    s = Solution()
    l = ["eat", "tea", "tan", "ate", "nat", "bat"]
    l2 = ["cab", "pug", "pei", "nay", "ron",
          "rae", "ems", "ida", "mes"]
    l3 = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(s.groupAnagrams(l),
          s.groupAnagrams(l2),
          s.groupAnagrams(l3),
          sep='\n\n')