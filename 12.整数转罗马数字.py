#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'
            }
        res = ''
        while num>0:
            for i in d.keys():
                if i <= num:
                    num -= i
                    res+=d[i]
                    break
        return res
# @lc code=end

