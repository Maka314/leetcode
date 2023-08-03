#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = self.backTracking(s,0,wordDict)
        return res

    def backTracking(self,s,position,wordDict):
        if position == len(s):
            return True

        for word in wordDict:
            if s[position:position+len(word)] == word:
                if self.backTracking(s,position+len(word),wordDict):
                    return True
        return False
# @lc code=end

