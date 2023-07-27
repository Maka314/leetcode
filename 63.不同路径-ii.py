#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ySize,xSize = len(obstacleGrid), len(obstacleGrid[0])
        routeMap = [[-1 for _ in range(xSize)] for _ in range(ySize)]
        for y in range(ySize):
            for x in range(xSize):
                upperBlock = bool(y == 0 or obstacleGrid[y-1][x]==1)
                leftBlock = bool(x == 0 or obstacleGrid[y][x-1]==1)
                if x==0 and y==0:
                    routeMap[y][x]=1
                elif upperBlock and leftBlock:
                    routeMap[y][x]=0
                elif upperBlock and not leftBlock:
                    routeMap[y][x] = routeMap[y][x-1]
                elif not upperBlock and leftBlock:
                    routeMap[y][x] = routeMap[y-1][x]
                else:
                    routeMap[y][x] = routeMap[y-1][x] + routeMap[y][x-1]
                
                if obstacleGrid[y][x]==1:
                    routeMap[y][x]=0
        return routeMap[ySize-1][xSize-1]
# @lc code=end

