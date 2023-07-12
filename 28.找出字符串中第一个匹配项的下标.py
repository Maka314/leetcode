#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i,j in enumerate(haystack):
            if j == needle[0] and haystack[i:i+len(needle)]==needle:
                return i
        return -1
# @lc code=end

