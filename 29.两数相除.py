#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res
# @lc code=end

