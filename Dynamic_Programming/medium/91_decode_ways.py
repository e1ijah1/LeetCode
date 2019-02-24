
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

1. 0不能单独解码 2. 两位数必须在1与26之间。这道题目实际上是用DP去做，仔细想的话，
可以发现就是约束版的f(n) = f(n-1) + f(n-2);，其中如果是s[n-1]为0，
f(n-1) = 0，f(n) = f(n-2)，因为0无法单独解码，而f(n-2)的条件则是必须在1与26之间，
否则f(n) = f(n-1)

"226"
"2222222222"
"126262626224882099"
"0"
"""


def num_decodings(s):
    # 寻找最优子结构和重叠子问题，以记忆化搜索或动态规划来解决
    if not s:
        return 0

    # memo[i] 表示字符串中第 i 位数字与其之后数字的组成的编码总数
    memo = [0 for _ in range(len(s))]
    if s[-1] != '0':
        memo[-1] = 1

    start = len(s)-2
    for i in range(start, -1, -1):
        # '0' 需要与其前一位一起考虑，不单独考虑
        if s[i] == '0':
            continue
        # 判断与后面的数字的组合是否小于 26
        if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
            if i == start:
                memo[i] = memo[i + 1] + 1
            else:
                # 以 i 位数字开头的编码总和其实就是其后两位数字各自的编码之和
                memo[i] = memo[i + 1] + memo[i + 2]
        else:
            memo[i] = memo[i + 1]
    return memo[0]
