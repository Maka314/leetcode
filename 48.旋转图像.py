#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        isOdd = size%2

        if isOdd:
            maxX = int(size/2+0.5)
            maxY = int(size/2-0.5)
        else:
            maxX,maxY = int(size/2),int(size/2)

        for y in range(maxY):
            for x in range(maxX):
                # 四角的坐标分别是
                # [x,y],   [size-y,x]
                # [size-x,size-y],[y,size-x]
                #1->2
                temp = [matrix[y][x],
                        matrix[x][size-y-1],
                        matrix[size-y-1][size-x-1],
                        matrix[size-x-1][y]]
                matrix[y][x]=temp[3]
                matrix[x][size-y-1]=temp[0]
                matrix[size-y-1][size-x-1]=temp[1]
                matrix[size-x-1][y]=temp[2]
# @lc code=end

