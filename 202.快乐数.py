#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        history = set()
        while n not in history:
            history.add(n)
            s = 0
            while n:
                s += (n % 10)**2
                n = n // 10
            n = s
            if n == 1:
                return True
        return False
# @lc code=end

