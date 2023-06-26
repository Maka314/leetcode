#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        dis = [set() for i in range(n)]
        for p1,p2 in dislikes:
            dis[p1-1].add(p2-1)
            dis[p2-1].add(p1-1)
        red,blue = set(),set()
        print(len(dis))
        for i,j in enumerate(dis):
            if i not in red and i not in blue:
                #两边都不排斥这个元素
                red.add(i)
                for hater in j:
                    if hater in red:
                        return False
                    else:
                        blue.add(hater)
            elif i in red and i not in blue:
                for hater in j:
                    if hater in red:
                        return False
                    else:
                        blue.add(hater)
            elif i not in red and i in blue:
                for hater in j:
                    if hater in blue:
                        return False
                    else:
                        red.add(hater)
            else:
                return False
        return True
                
# @lc code=end

