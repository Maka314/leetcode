#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x,y,i=0,0,2
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        matrix[0][0]=1
        while True:
            while x+1<n and matrix[y][x+1]==0:
                x+=1
                matrix[y][x]=i
                i+=1
            while y+1<n and matrix[y+1][x]==0:
                y+=1
                matrix[y][x]=i
                i+=1
            while x>0 and matrix[y][x-1]==0:
                x-=1
                matrix[y][x]=i
                i+=1
            while y>0 and matrix[y-1][x]==0:
                y-=1
                matrix[y][x]=i
                i+=1
            if i > n**2:
                return matrix
# @lc code=end

