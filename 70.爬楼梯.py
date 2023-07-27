#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.slution = {1:1,
                        2:2}

    def climbStairs(self, n: int) -> int:
        if n in self.slution:
            return self.slution[n]
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.slution[n] = res
        return res
# @lc code=end

