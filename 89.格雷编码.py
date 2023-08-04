#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        self.res = {1:[0, 1]}
        return self.construct(n)

    def construct(self, n):
        if n in self.res:
            return self.res[n]
        
        lastRes = self.construct(n-1)
        res = lastRes + [i+2**(n-1) for i in lastRes[::-1]]
        #运用反射编码性质
        self.res[n] = res
        return res
# @lc code=end

