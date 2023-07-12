#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        size = len(s)
        res = ''
        cycle = size // (2 * k) + 1
        print(cycle)
        left = size % (2 * k)
        for c in range(cycle):
            res += s[2*k*c:2*k*c+k][::-1] + s[2*k*c+k:2*k*c+2*k]
        return res
# @lc code=end

