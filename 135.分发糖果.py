#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = 1
        candyForYou = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyForYou += 1
                res += candyForYou
            elif ratings[i] < ratings[i - 1]:
                candyForYou -= 1
                if candyForYou:
                    res += candyForYou
                else:
                    candyForYou = 1
                    res += i + 1
            else:
                candyForYou -= 1
                if candyForYou == 0:
                    candyForYou = 1
                res += candyForYou
        return res
# @lc code=end

