#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        res = []
        print(count)
        while k:
            m = 0
            for i in count:
                if count[i] > m:
                    m = count[i]
                    mi = i
            count[mi] = 0
            res += [mi]
            k -= 1
        return res
# @lc code=end

