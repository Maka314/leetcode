#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.maxResult = {
            1:1,
            2:1
        }
    def integerBreak(self, n: int) -> int:
        if n in self.maxResult:
            return self.maxResult[n]
        res = [] #浪费
        for i in range(1,n):
            res.append(i*max(self.integerBreak(n - i), n-i))
        res = max(res)
        self.maxResult[n] = res
        return res
# @lc code=end

