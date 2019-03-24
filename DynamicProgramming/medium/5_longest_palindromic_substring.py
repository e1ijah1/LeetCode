

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def longest_palindrome(s: str) -> str:
    """
    Manacher's Algorithm Solution
    :param s:
    :return:
    """
    if not s:
        return s

    # after join, len will be n + n-1, add # at head & tail, len will be 2n + 1
    # so len will always a odd num
    s2 = '^#' + '#'.join(c for c in s) + '#$'
    l = [0 for _ in s2]

    icenter = iright = imax = 0

    for i in range(1, len(l)):
        if len(l) - 1 - i <= l[imax]:
            break

        """
        维护最右边界, min 是整合右边界内及左越界的情况
        iright - i 较 l[imirror] 小时, 超出的部分无法界定, 留给朴素计算 
        """
        if i < iright:
            imirror = 2 * icenter - i
            l[i] = min(iright - i, l[imirror])

        # 以中心计算回文长度, 此算法中长度不包括中心, 仅为对称的长度
        while s2[i + l[i] + 1] == s2[i - l[i] - 1]:
            l[i] += 1

        if iright < i + l[i]:
            icenter = i
            iright = i + l[i]

        if l[imax] < l[i]:
            imax = i

    re = s2[(imax - l[imax]):(imax + l[imax])]
    return re.replace('#', '')
