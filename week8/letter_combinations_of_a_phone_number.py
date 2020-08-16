from typing import List


class Solution:
    def __init__(self):
        self.buttons = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = self.process(digits, 0)
        return res

    def process(self, digits: str, i: int):
        if i == len(digits) - 1:
            return self.buttons[digits[i]]

        chs = self.buttons[digits[i]]
        strs = self.process(digits, i + 1)
        res = [ch + s for ch in chs for s in strs]

        return res

