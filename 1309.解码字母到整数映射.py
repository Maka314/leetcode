#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        res = []
        while i >= 0:
            if s[i] == '#':
                res.append(chr(96 + int(s[i-2:i])))
                i -= 3
            else:
                res.append(chr(96 + int(s[i])))
                i -= 1
        return ''.join(res[::-1])
# @lc code=end

