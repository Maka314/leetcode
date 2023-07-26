#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        strNum = str(N)

        flag = len(strNum)
        
        for i in range(len(strNum) - 1, 0, -1):
            if strNum[i - 1] > strNum[i]:
                flag = i  # 更新flag的值，记录需要修改的位置
                # 将前一个字符减1，以保证递增性质
                strNum = strNum[:i - 1] + str(int(strNum[i - 1]) - 1) + strNum[i:]
        
        # 将flag位置及之后的字符都修改为9，以保证最大的递增数字
        for i in range(flag, len(strNum)):
            strNum = strNum[:i] + '9' + strNum[i + 1:]
        
        # 将最终的字符串转换回整数并返回
        return int(strNum)
# @lc code=end

