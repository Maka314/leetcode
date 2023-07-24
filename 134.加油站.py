#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startIndex, currentIndex = 0, 0
        gasTank = 0
        siteNum = len(gas)
        while startIndex < siteNum and (currentIndex - startIndex < siteNum):
            gasTank = gasTank + gas[currentIndex % siteNum] - cost[currentIndex % siteNum]
            currentIndex += 1
            if gasTank < 0:
                startIndex, gasTank = currentIndex, 0
        if startIndex >= siteNum:
            return -1
        else:
            return startIndex
# @lc code=end

