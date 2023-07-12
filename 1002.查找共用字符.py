#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = list(words[0])
        for w in words[1:]:
            tempWord = list(w)
            res = res and tempWord
        return res
# @lc code=end

