#
# @lc app=leetcode.cn id=1499 lang=python3
#
# [1499] 满足不等式的最大值
#


# @lc code=start
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = []  # 数据结构为[xi，yi-xi]
        res = float("-inf")

        for cElement in points:
            while queue and cElement[0] - queue[0][0] > k:
                queue.pop(0)
            
            if queue:
                res = max(res, queue[0][1] + cElement[0] + cElement[1])

            while queue and (cElement[1] - cElement[0]) >= queue[-1][1]:
                queue.pop()

            queue.append([cElement[0], (cElement[1] - cElement[0])])

        return res
        #test

# @lc code=end
