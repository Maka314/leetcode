#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.f = {0:0,
                  1:1,
                  2:1}

    def fib(self, n: int) -> int:
        if n in self.f:
            return self.f[n]
        res = self.fib(n-1) + self.fib(n-2)
        self.f[n] = res
        return res
# @lc code=end

