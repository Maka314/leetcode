#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        import math
        res = []
        xcount,ycount = len(matrix[0]),len(matrix)
        round = math.ceil(min(xcount,ycount)/2)
        for r in range(round):
            #第一轮向右
            y = r
            for x in range(r,xcount-r):
                res.append(matrix[y][x])
            #第二轮向下
            x = xcount-1-r
            for y in range(r+1,ycount-r):
                res.append(matrix[y][x])
            #第三轮向左
            y = ycount-1-r
            for x in range(xcount-2-r,r-1,-1):
                res.append(matrix[y][x])
            #第四轮向上
            x = r
            for y in range(ycount-2-r,r,-1):
                res.append(matrix[y][x])
        return res
# @lc code=end