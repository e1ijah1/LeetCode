# -*- coding: utf-8 -*-
# Created by f1renze on 18-7-4 下午1:51
__author__ = 'f1renze'
__time__ = '18-7-4 下午1:51'

'''
40ms

给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:
s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
'''


def decode_string(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    cur_num = 0
    cur_str = ''
    for item in s:
        if item == '[':
            stack.append(cur_num)
            stack.append(cur_str)
            # 入栈归零
            cur_num = 0
            cur_str = ''
        elif item == ']':
            pre_str = stack.pop()
            num = stack.pop()
            cur_str = pre_str + num * cur_str
        elif item.isdigit():
            # 多位数进位
            cur_num = cur_num * 10 + int(item)
        else:
            cur_str += item
    return cur_str


if __name__ == '__main__':
    t1 = "3[a]2[bc]"
    t2 = "100[leetcode]"
    print(decode_string(t2))
