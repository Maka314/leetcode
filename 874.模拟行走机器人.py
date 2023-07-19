#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#


# @lc code=start
# 方向1，2，3，4，分别是上，右，下，左
# 坐标格式为[x, y]
class navigator:
    def __init__(self, obstacles) -> None:
        self.barrierX = {}  # 以X查询障碍物
        self.barrierY = {}  # 以Y查询障碍物
        for i in obstacles:
            # i[0] is X, i[1] is Y
            if i[0] in self.barrierX:
                self.barrierX[i[0]].add(i[1])
            else:
                self.barrierX[i[0]] = set([i[1]])
            if i[1] in self.barrierY:
                self.barrierY[i[1]].add(i[0])
            else:
                self.barrierY[i[1]] = set([i[0]])

    def move(self, location, direction, distance):
        if direction in [1, 3]:
            # 上下方向
            d = 1 if direction == 1 else -1
            if location[0] not in self.barrierX:
                location[1] += d * distance
            else:
                for _ in range(distance):
                    location[1] += 1 * d
                    if location[1] in self.barrierX[location[0]]:
                        location[1] -= 1 * d
                        break
        else:
            # 左右方向
            d = 1 if direction == 2 else -1
            if location[1] not in self.barrierY:
                location[0] += d * distance
            else:
                for _ in range(distance):
                    location[0] += 1 * d
                    if location[0] in self.barrierY[location[1]]:
                        location[0] -= 1 * d
                        break
        return location


class bot:
    def __init__(self) -> None:
        self.direction = 1
        self.location = [0, 0]

    def turn(self, commend):
        if commend == -1:
            self.direction += 1
            if self.direction > 4:
                self.direction = 1
        elif commend == -2:
            self.direction -= 1
            if self.direction < 1:
                self.direction = 4
        return self.direction


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        playGround = navigator(obstacles)
        b = bot()
        res = 0
        for commend in commands:
            if commend < 0:
                b.turn(commend)
            else:
                b.location = playGround.move(b.location, b.direction, commend)
                res = max(res, (b.location[0] ** 2 + b.location[1] ** 2))
        return res

# @lc code=end
