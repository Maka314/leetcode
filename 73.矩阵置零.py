#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ySize,xSize = len(matrix),len(matrix[0])
        bombInLine = True if 0 in matrix[0] else False
        bombinColumn = False
        for y in range(ySize):
            if not matrix[y][0]:
                bombinColumn = True
        for x in range(1,xSize):
            for y in range(1,ySize):
                if matrix[y][x]==0:
                    matrix[0][x],matrix[y][0]=0,0

        for x in range(1,xSize):
            if matrix[0][x]==0:
                for y in range(ySize):
                    matrix[y][x]=0
        for y in range(1,ySize):
            if matrix[y][0]==0:
                for x in range(xSize):
                    matrix[y][x]=0

        if bombInLine:
            for x in range(xSize):
                matrix[0][x]=0
        if bombinColumn:
            for y in range(ySize):
                matrix[y][0]=0
# @lc code=end

