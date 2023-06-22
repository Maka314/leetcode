#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        p = 1
        if x < 0:
            x = -x
            p = -1
        while x:
            res = 10*res + x%10
            x = x//10
            if res >= 2147483648:
                return 0
                break
        if p==-1:
            return -res
        elif res == 2147483648:
            return 0
        else:
            return res
# @lc code=end

