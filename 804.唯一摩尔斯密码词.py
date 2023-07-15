#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#


# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        res = set()
        for w in words:
            code = ""
            for c in w:
                code += morse[ord(c) - 97]
            res.add(code)
        return len(res)


# @lc code=end
