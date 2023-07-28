#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x in range(len(board[0])):
            for y in range(len(board)):
                if self.backTracking(board, word, [], x, y):
                    return True
        return False

    def backTracking(self, board, word, path, x, y):
        if x < 0 or x >= len(board[0]):
            return False
        if y < 0 or y >= len(board):
            return False
        if word[len(path)] != board[y][x]:
            return False

        path.append(board[y][x])
        board[y][x] = "0"
        if len(path) == len(word):
            return True

        if (
            self.backTracking(board, word, path, x, y + 1)
            or self.backTracking(board, word, path, x + 1, y)
            or self.backTracking(board, word, path, x, y - 1)
            or self.backTracking(board, word, path, x - 1, y)
        ):
            return True

        board[y][x] = path.pop()
        return False


# @lc code=end
