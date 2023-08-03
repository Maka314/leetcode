#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        plan = [0 for _ in range(n+1)]
        plan[0] = 1
        for stares in range(n-1):
            plan[stares+2] += plan[stares]
            plan[stares+1] += plan[stares]
        
        return plan[-1]+plan[-2]
# @lc code=end

