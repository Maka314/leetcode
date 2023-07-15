#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        res, i = "", 0
        size = len(s)
        while i < size:
            if ord(s[i]) in range(48,58):
                count = 0
                while ord(s[i]) in range(48,58):
                    count = 10 * count + int(s[i])
                    i += 1
                repeater = ""
                i += 1
                while s[i] != ']':
                    repeater += s[i]
                    i += 1
                i += 1
                res += repeater * count
            else:
                res += s[i]
                i += 1
        return res
# @lc code=end

