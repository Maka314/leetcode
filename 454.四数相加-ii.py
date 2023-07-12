#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        resList1, resList2, resList3, resList4 = {},{},{},{}
        for i,j in enumerate(nums1):
            if j not in resList1:
                resList1[j] = 1
            else:
                resList1[j] += 1
        for i,j in enumerate(nums2):
            for res in resList1:
                if (res + j) not in resList2:
                    resList2[res + j] = resList1[res]
                else:
                    resList2[res + j] += resList1[res]
        for j in nums3:
            for res in resList2:
                if res + j not in resList3:
                    resList3[res + j] = resList2[res]
                else:
                    resList3[res + j] += resList2[res]
        for j in nums4:
            for res in resList3:
                if res + j not in resList4:
                    resList4[res + j] = resList3[res]
                else:
                    resList4[res + j] += resList3[res]
        if 0 in resList4:
            return resList4[0]
        else:
            return 0
# @lc code=end

