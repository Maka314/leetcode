#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648:
            return 2147483647
        mark = True
        res = 0
        if dividend<0:
            dividend = -dividend
            mark = not mark
        if divisor<0:
            divisor = -divisor
            mark = not mark
        while dividend>0:
            dividend-=divisor
            res+=1
        if dividend<0:
            res-=1
        if not mark:
            res = -res
        return res
# @lc code=end

