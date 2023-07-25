#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort(key = lambda x : (x[0], x[1]))
        res = 1
        shotP = min(points[0][1], points[1][1])
        for i,ball in enumerate(points[1:]):
            if shotP >= ball[0] and shotP <= ball[1]:
                pass #命中
            else:
                #未命中
                res+=1
                if i < len(points)-1:
                    shotP = min(ball[1], points[i+1][1])
                else:
                    shotP = ball[1]
        return res
# @lc code=end

