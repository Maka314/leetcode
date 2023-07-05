#
# @lc app=leetcode.cn id=2600 lang=python3
#
# [2600] K 件物品的最大和
#

# @lc code=start
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        oneItem = numOnes if numOnes<=k else k
        negativeItem = 0 if k<=(numOnes+numZeros) else (numOnes+numZeros-k)
        return oneItem+ negativeItem
# @lc code=end

