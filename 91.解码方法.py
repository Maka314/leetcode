#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0 for _ in range(len(s) + 1)]

        res[0] = 1

        # 第一位特殊判断
        if int(s[0]) >= 1 and int(s[0]) <= 9:
            res[1] = 1

        # 第二位开始循环
        for i in range(1, len(s)):
            oneDigit = int(s[i])
            twoDigit = int(s[i - 1 : i + 1])
            if oneDigit >= 1 and oneDigit <= 9:
                res[i + 1] += res[i]
            if twoDigit >= 10 and twoDigit <= 26:
                res[i + 1] += res[i - 1]

        return res[-1]


# @lc code=end
