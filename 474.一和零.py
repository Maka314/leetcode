#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        bag = [[0 for zeroLenth in range(m+1)] for oneLenth in range(n+1)]
        #bag[1_limit][0_limit]

        for item in strs:

            zeroCount = item.count('0')
            oneCount = item.count('1')

            for one_limit in range(n,-1,-1):
                for zero_limit in range(m,-1,-1):
                    if zero_limit >= zeroCount and one_limit >= oneCount and (bag[one_limit - oneCount][zero_limit - zeroCount] + 1 > bag[one_limit][zero_limit]):
                        bag[one_limit][zero_limit] = bag[one_limit - oneCount][zero_limit - zeroCount] + 1
        
        return bag[n][m]
# @lc code=end

