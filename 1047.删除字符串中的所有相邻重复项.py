#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        a, i = list(s), 1
        while i<len(a):
            if a[i-1] == a[i]:
                a.pop(i - 1)
                a.pop(i - 1)
                if i > 1:
                    i -= 1
            else:
                i += 1
        return ''.join(a)
# @lc code=end

