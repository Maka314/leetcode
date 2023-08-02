#
# @lc app=leetcode.cn id=822 lang=python3
#
# [822] 翻转卡片游戏
#

# @lc code=start
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        repeat = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                repeat.add(fronts[i])
        nums = set(fronts+backs)
        for n in nums:
            if n not in repeat:
                return n
        return 0
# @lc code=end

