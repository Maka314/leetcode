#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphaBank = {}
        for c in magazine:
            if c in alphaBank:
                alphaBank[c] += 1
            else:
                alphaBank[c] = 1
        for c in ransomNote:
            if c not in alphaBank:
                return False
            else:
                alphaBank[c] -= 1
        for c in alphaBank:
            if alphaBank[c] < 0:
                return False
        return True
# @lc code=end

