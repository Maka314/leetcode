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
            if ord(s[i]) in range(48, 58):
                count = 0
                while ord(s[i]) in range(48, 58):
                    count = 10 * count + int(s[i])
                    i += 1
                # 此时i下标位置为左边括号
                startPoint, layer = i + 1, 1
                while layer:
                    i += 1
                    if s[i] == "[":
                        layer += 1
                    elif s[i] == "]":
                        layer -= 1
                # 此时i下标位置为右括号
                repeater = self.decodeString(s[startPoint:i])
                res += repeater * count
                i += 1
            else:
                res += s[i]
                i += 1
        return res


# @lc code=end
