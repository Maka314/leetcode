#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        while True:
            b = res * res
            if b == x:
                return res
            elif b > x:
                return res - 1
            else:
                res += 1
# @lc code=end

