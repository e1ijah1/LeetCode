# -*- coding: utf-8 -*-
# Created by f1renze on 18-6-4 下午9:39
__author__ = 'f1renze'
__time__ = '18-6-4 下午9:39'

import sys
import os

# 导入同级目录下的模块(sys.path.append), 里面的表达式获取此模块所在的目录
sys.path.append(os.path.dirname(os.path.abspath('__file__')))
# 从模块导入类
from SStack import SStack

'''
p142 5.3.2 表达式的表示, 计算和变换

中缀表示形式, 二元运算符写在两个运算对象中间
前缀表示形式, 将函数符号写在运算对象前面, 又称波兰表达式
后缀表示形式, 运算符写在运算对象之后, 特别适合计算机处理, 又称逆波兰表达式

同一个算术表达式的三种等价表示形式:
中缀形式: (3 - 5) * (6 + 17 * 4) / 3
前缀形式: / * - 3 5 + 6 * 17 4 3
后缀形式: 3 5 - 6 17 4 * + * 3 / 1

后缀表达式计算:
- 遇到运算对象时, 记录备用
- 遇到运算符(或函数名), 应该根据其元数(这里都是二元运算符), 取得前面最近
遇到的几个运算对象或已完成运算的结果(二元运算符取2个), 应用运算符计算并保存结果.
'''


class ESStack(SStack):
    """
    算法框架:
        while <存在输入>:
            x = nextItem()          # 假设此函数返回表达式中的下一个项
            if is_operand(x):       # 若为运算对象, 转换为浮点数并入栈
                st.push(float(x))
            else:                   # 否, 为(二元)运算符
                a = st.pop()        # 第二个运算对象
                b = st.pop()        # 第一个运算对象
                ...                 # 根据运算符 x 对 a 和 b 计算
                ...                 # 计算结果压入栈
    因为此种算法不能处理栈中元素不足2个的情况, 所以需要检查栈的深度,
    这里继承顺序表实现的栈数据结构类, 增加检查栈深度的方法
    """
    def depth(self):
        return len(self._elem)


def suf_exp_evaluator(exp):
    operators = '+-*/'
    st = ESStack()
    for x in exp:
        # 非操作符入栈, 不能转换为浮点数抛出异常
        if x not in operators:
            st.push(float(x))
            continue
        # 此时 x 非操作符, 若栈深度小于 2 无法操作
        if st.depth() < 2:
            # operand 操作数
            raise SyntaxError('Short of operand(s).')
        # 取得2个运算对象
        a = st.pop()
        b = st.pop()
        c = None
        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            # b / 0 时会抛出 ZeroDivisionError: division by zero
            c = b / a
        # 计算结果入栈
        st.push(c)
    # 表达式中的项迭代完后栈深度不为1抛出异常
    if st.depth() == 1:
        return st.pop()
    # 额外的操作数d
    raise SyntaxError('Extra operand(s).')


def suffix_exp_evaluator(line_):
    # 默认表达式中的项和运算符之间都有空格, split() 除去空格返回一个 list
    return suf_exp_evaluator(line_.split())


def suffix_exp_calculator():
    """
    定义了一个交互式的驱动函数, 输入 end 结束
    :return: None
    """
    while True:
        try:
            line = input('Suffix Expression: ')
            if line == 'end':
                return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as e:
            print('Error:', type(e), e.args)


if __name__ == '__main__':
    '''
    >>> (3 - 5) * (6 + 17 * 4) / 3
    -49.333333333333336
    输入: 3 5 - 6 17 4 * + * 3 /
    输出: 等同于中缀表示形式
    '''
    suffix_exp_calculator()
