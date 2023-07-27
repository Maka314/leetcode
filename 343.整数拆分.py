#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.maxResult = {
            0:0,
            1:1,
            2:1
        }
    def integerBreak(self, n: int) -> int:
        if n in self.maxResult:
            return self.maxResult[n]
        res = []
        for i in range(1,n):
            res.append(max(i * self.integerBreak(n - i), i * (n-i)))
        res = max(res)
        self.maxResult[n] = res
        return res
# @lc code=end

