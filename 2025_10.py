"""
question https://adventofcode.com/2025/day/10
answer ref https://github.com/Y0UR-U5ERNAME/Advent-of-Code/blob/main/2025/day10.py
"""


def solve(light, buttons):
    light = sum(j << c for c, j in enumerate(light))
    buttons = [sum(1 << c for c in b) for b in buttons]

    def rsolve(light, idx=0):
        if light == 0:
            return 0
        if idx == len(buttons):
            return float("inf")
        res = min(rsolve(light, idx + 1), 1 + rsolve(light ^ buttons[idx], idx + 1))
        return res

    res = rsolve(light)
    return res if res != float("inf") else -1


a = solve([0, 1, 1, 0], [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]])
print(a)
