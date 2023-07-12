#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for i in range(size-1,0,-1):
            if size % i:
                continue
            elif s[:i]*(size//i) == s:
                return True
        return False
# @lc code=end

