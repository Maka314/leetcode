#
# @lc app=leetcode.cn id=2208 lang=python3
#
# [2208] 将数组和减半的最少操作次数
#

# @lc code=start
from heapq import heappush
from heapq import heappop

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums) / 2
        h = []
        for v in nums:
            heappush(h, -v)
        ans = 0
        while s > 0:
            t = -heappop(h) / 2
            s -= t
            heappush(h, -t)
            ans += 1
        return ans
# @lc code=end

