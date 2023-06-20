#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        xcount,ycount = len(matrix[0]),len(matrix)
        res = [None for i in range(xcount*ycount)]
        for iy,jy in enumerate(matrix):
            for ix,jx in enumerate(jy):
                res[iy*xcount+ix] = jx
        return res
# @lc code=end