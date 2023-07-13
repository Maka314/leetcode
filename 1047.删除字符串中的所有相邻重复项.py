#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if not res:
                res.append(c)
            elif c == res[-1]:
                res.pop()
            else:
                res.append(c)
        return ''.join(res)
# @lc code=end

