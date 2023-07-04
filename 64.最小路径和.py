#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ySize,xSize = len(grid),len(grid[0])
        sumMap = [[0 for _ in range(xSize)] for _ in range(ySize)]
        sumMap[0][0] = grid[0][0]
        for x in range(1,xSize):
            sumMap[0][x] = sumMap[0][x-1]+grid[0][x]
        for y in range(1,ySize):
            sumMap[y][0] = sumMap[y-1][0]+grid[y][0]
        for y in range(1,ySize):
            for x in range(1,xSize):
                sumMap[y][x] = grid[y][x]+min(sumMap[y-1][x],sumMap[y][x-1])
        return sumMap[ySize-1][xSize-1]
# @lc code=end

