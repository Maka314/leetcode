#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backTracking(board, 0, 0)

    def boardCheck(self, board, x, y):
        for xi in range(9):
            if board[y][xi] == board[y][x] and xi != x:
                return False
        for yi in range(9):
            if board[yi][x] == board[y][x] and yi != y:
                return False
        ySquare, xSquare = y // 3, x // 3
        for yi in range(3 * ySquare, 3 * (ySquare + 1)):
            for xi in range(3 * xSquare, 3 * (xSquare + 1)):
                if board[yi][xi] == board[y][x] and not (xi == x and yi == y):
                    return False
        return True

    def backTracking(self, board, x, y):
        if y == 8 and x == 8 and board[y][x] != '.':
            return True

            

        if board[y][x] != ".":
            if self.boardCheck(board, x, y):
                if x == 8:
                    return self.backTracking(board, 0, y + 1)
                else:
                    return self.backTracking(board, x + 1, y)
            else:
                return False

        for i in range(1,10):
            board[y][x] = str(i)
            if self.boardCheck(board,x,y):
                if x == 8 and y == 8:
                    return True
                if x == 8:
                    res = self.backTracking(board, 0, y + 1)
                else:
                    res = self.backTracking(board, x + 1, y)
                
                if res:
                    return True
        board[y][x] = '.'
        return False

# @lc code=end
