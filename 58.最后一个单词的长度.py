#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for l,j in enumerate(s[::-1]):
            if j!=' ':
                break
        if l:
            s = s[:-l]
        
        for i,j in enumerate(s[::-1]):
            if j ==' ':
                return i
        return len(s)
# @lc code=end

