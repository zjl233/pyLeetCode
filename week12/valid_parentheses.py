class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stack = []
        for p in s:
            if p not in d:
                stack.append(p)
            else:
                if not stack or stack.pop() != d[p]:
                    return False

        return len(stack) == 0
