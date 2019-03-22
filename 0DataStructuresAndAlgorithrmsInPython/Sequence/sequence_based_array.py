class GameEntry:
    """记录游戏条目"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"{self._name}, {self._score}"


class Scoreboard:
    """

    """

    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, item):
        return self._board[item]

    def __str__(self):
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """
        新增分数必须大于已有的最低分数, 若 board 满, 最低分会被丢弃
        :param entry:
        :return:
        """
        score = entry.get_score()

        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry


def insertion_sort(l):
    """
    插入排序, 时间 O(n^2)
    :param l:
    :return:
    """
    for k in range(1, len(l)):
        cur, j = l[k], k
        while j > 0 and l[j - 1] > cur:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1


if __name__ == "__main__":
    sb = Scoreboard()
    e = GameEntry("Jack", 100)
    sb.add(e)
    sb.add(GameEntry("Marry", 200))
    print(sb)
