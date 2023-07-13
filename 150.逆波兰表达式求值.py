#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens) -> int:
        calculater = set(['+', '-', '*', '/'])
        numberStack = []
        for t in tokens:
            if t not in calculater:
                numberStack.append(int(t))
            else:
                if t == '+':
                    numberStack.append(numberStack.pop() + numberStack.pop())
                elif t == '-':
                    temp = numberStack.pop()
                    numberStack.append(numberStack.pop() - temp)
                elif t == '*':
                    numberStack.append(numberStack.pop() * numberStack.pop())
                else:
                    temp = numberStack.pop()
                    numberStack.append(int(numberStack.pop() / temp))
        return numberStack[-1]
# @lc code=end

