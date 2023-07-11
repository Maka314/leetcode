#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        for c in s:
            if c in ds:
                ds[c] += 1
            else:
                ds[c] = 1
        for c in t:
            if c not in ds:
                return False
            else:
                ds[c] -= 1
        for e in ds:
            if ds[e] != 0:
                return False
        return True
# @lc code=end

