#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,ySize = 0, len(matrix)
        while i<ySize-1 and matrix[i][0]<=target:
            if matrix[i+1][0]>target:
                if target in matrix[i]:
                    return True
                else:
                    return False
                break
            i+=1
        if target in matrix[-1]:
            return True
        return False

# @lc code=end

