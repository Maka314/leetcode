#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        routeHistory={'1 1':1}
        def pathFinder(m,n):
            if str(m)+' '+str(n) in routeHistory:
                return routeHistory[str(m)+' '+str(n)]
            elif m==1 or n==1:
                return 1
            else:
                routeHistory[str(m-1)+' '+str(n)] = pathFinder(m-1,n)
                routeHistory[str(m)+' '+str(n-1)] = pathFinder(m,n-1)
                return routeHistory[str(m-1)+' '+str(n)]+routeHistory[str(m)+' '+str(n-1)]
        return pathFinder(m,n)
# @lc code=end