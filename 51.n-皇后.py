#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.backTracking([],n)
        return self.res

    def backTracking(self,path,n):
        if len(path) == n:
            r = []
            for p in path:
                r.append("")
                r[-1] += '.' * p
                r[-1] += 'Q'
                r[-1] += '.' * (n - p - 1)
            self.res.append(r)
            return

        path.append(0)
        for i in range(n):
            path[-1] = i
            queenFlag = True
            for line in range(len(path)-1):
                if path[line] == i or abs(path[line]-i) == len(path)-1-line:
                    queenFlag = False
                    break
            if queenFlag:
                self.backTracking(path,n)
        path.pop()
# @lc code=end

