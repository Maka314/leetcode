#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        bag = [False for _ in range(len(s) + 1)]
        bag[0] = True
        for position in range(1, len(s) + 1):
            for item in wordDict:
                if len(item) <= position and s[position - len(item) : position] == item:
                    if bag[position - len(item)]:
                        bag[position] = True
                        break
        return bag[-1]


# @lc code=end
