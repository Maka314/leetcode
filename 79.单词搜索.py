#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        for x in range(len(self.board[0])):
            for y in range(len(self.board)):
                if self.board[y][x] == word[0] and self.backTracking([], x, y):
                    return True
        return False

    def backTracking(self, path, x, y):
        path.append(self.board[y][x])
        if len(path) == len(self.word):
            return True
        self.board[y][x] = 0
        res = False
        if y - 1 >= 0 and self.board[y - 1][x] == self.word[len(path)]:
            res = self.backTracking(path, x, y - 1)
        if (
            (not res)
            and x + 1 < len(self.board[0])
            and self.board[y][x + 1] == self.word[len(path)]
        ):
            res = self.backTracking(path, x + 1, y)
        if (
            (not res)
            and y + 1 < len(self.board)
            and self.board[y + 1][x] == self.word[len(path)]
        ):
            res = self.backTracking(path, x, y + 1)
        if (
            (not res)
            and (x - 1 >= 0)
            and (self.board[y][x - 1] == self.word[len(path)])
        ):
            res = self.backTracking(path, x - 1, y)

        if not res:
            self.board[y][x] = path[-1]
            path.pop

        return res


# @lc code=end
