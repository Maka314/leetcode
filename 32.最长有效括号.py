#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res,stack = 0,0
        d = [0 for i in range(len(s))]
        for i,j in enumerate(s):
            if j=='(':
                stack+=1
            else:
                stack-=1
            if not stack:
                pass
        return res
# @lc code=end

