#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        useableNum = [i**2 for i in range(1, int(n**0.5) + 1)]
        bag = [n for _ in range(n + 1)]
        bag[0] = 0

        for num in useableNum:
            for s in range(n+1):
                if s - num >= 0:
                    bag[s] = min(bag[s], bag[s-num]+1)

        return bag[-1]
# @lc code=end

