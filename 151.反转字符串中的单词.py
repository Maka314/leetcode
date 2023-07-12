#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        s = ' '+s
        for i,j in enumerate(s):
            if j == ' ':
                continue
            elif s[i-1] == ' ':
                res.append('')
                res[-1] += j
            else:
                res[-1] += j
        return ' '.join(res[::-1])
# @lc code=end

