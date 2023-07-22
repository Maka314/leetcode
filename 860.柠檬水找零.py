#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashBox = {
            5:0,
            10:0,
            20:0
        }
        for bill in bills:
            cashBox[bill] += 1
            bill -= 5
            while bill >= 10 and cashBox[10]:
                bill -= 10
                cashBox[10] -= 1
            while bill >= 5 and cashBox[5]:
                bill -= 5
                cashBox[5] -= 1
            if bill:
                return False
        return True

# @lc code=end

