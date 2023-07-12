#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        abMap = {}
        cdMap = {}
        for i1 in nums1:
            for i2 in nums2:
                if i1 + i2 not in abMap:
                    abMap[i1 + i2] = 1
                else:
                    abMap[i1 + i2] += 1
        for i3 in nums3:
            for i4 in nums4:
                if i3 + i4 not in cdMap:
                    cdMap[i3 + i4] = 1
                else:
                    cdMap[i3 + i4] += 1
        res = 0
        for abSum in abMap:
            if -abSum in cdMap:
                res += abMap[abSum] * cdMap[-abSum]
        return res
# @lc code=end

