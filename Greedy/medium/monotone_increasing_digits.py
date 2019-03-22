"""
https://leetcode.com/problems/monotone-increasing-digits/
"""


class Solution:
    @staticmethod
    def get_digit_list(n):
        return list(map(int, str(n)))

    @staticmethod
    def convert_dl2int(dl):
        return int("".join([str(i) for i in dl]))

    def check_monotone_increasing_digits(self, n):
        dl = self.get_digit_list(n)
        return all(map(lambda x: x[0] <= x[1], zip(dl, dl[1:])))

    def find_not_incresing_digit(self, n):
        """
        eg: input 866, t1 = ((8, 6), (6, 6)), find = (8, 6)
        :param n:
        :return:
        """
        dl = self.get_digit_list(n)
        t1 = tuple(zip(dl, dl[1:]))
        find = list(filter(lambda x: x[0] > x[1], t1))[0]
        return tuple(t1).index(find)

    def get_num(self, n):
        """
        eg, 321 return 300
        :param n:
        :return:
        """
        dl = self.get_digit_list(n)
        nl = [dl[0]] + [0 for i in dl[1:]]
        # int(reduce(lambda x, y: str(x)+str(y), nl))
        return self.convert_dl2int(nl)

    def monotoneIncreasingDigits(self, n):
        """
        :type N: int
        :rtype: int
        """

        # 本身单调递增
        if self.check_monotone_increasing_digits(n):
            return n

        dl = self.get_digit_list(n)
        num = self.find_not_incresing_digit(n)
        """
        input 855832 
        判断这个数字中第几位开始不递增， 前一位 -1, 后续填9
        """
        for i in range(num, -1, -1):
            new_dl = dl[:i] + [dl[i] - 1] + [9 for i in dl[i + 1 :]]
            new = self.convert_dl2int(new_dl)
            if self.check_monotone_increasing_digits(new):
                return new

        # eg: input 332, check 301 ~ 331
        # for i in range(n - 1, num, -1):
        #     if self.check_monotone_increasing_digits(i):
        #         return i
        #
        # for i in range(num - 1, 0, -1):
        #     if self.check_monotone_increasing_digits(i):
        #         return i


if __name__ == "__main__":
    obj = Solution()
    print(obj.find_not_incresing_digit(332), obj.get_num(332))  # 299
    print(obj.find_not_incresing_digit(866), obj.get_num(866))
    print(obj.find_not_incresing_digit(120))  # 119
    print(obj.monotoneIncreasingDigits(120))
