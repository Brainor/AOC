"""
question https://adventofcode.com/2025/day/10
answer ref https://github.com/Y0UR-U5ERNAME/Advent-of-Code/blob/main/2025/day10.py
part 2:
z3: https://github.com/mgtezak/Advent_of_Code/blob/master/2025/10/p2.py
bifurcate: https://www.reddit.com/r/adventofcode/comments/1pk87hl/comment/ntp4njq/
"""


def solve(light, buttons):
    light = sum(j << c for c, j in enumerate(light))
    buttons = [sum(1 << c for c in b) for b in buttons]

    def rsolve(light, idx=0):
        if light == 0:
            return 0
        if idx == len(buttons):
            return float("inf")
        ## 迭代, 选择按或不按当前按钮, 取最小值
        res = min(rsolve(light, idx + 1), 1 + rsolve(light ^ buttons[idx], idx + 1))  # 位运算, 异或切换灯的状态
        return res

    res = rsolve(light)
    return res if res != float("inf") else -1


def solve(light, buttons):
    light = sum(j << c for c, j in enumerate(light))
    buttons = [sum(1 << c for c in b) for b in buttons]
    min_len = len(buttons) + 1

    def rsolve(light, pressed, idx):
        nonlocal min_len
        if light == 0:
            min_len = min(min_len, len(pressed))
            return pressed
        if len(pressed) > min_len or idx == len(buttons):
            return [-1] * (idx + 1)
        ## 迭代, 选择按或不按当前按钮, 取最小值
        press_state = rsolve(light ^ buttons[idx], pressed + [idx], idx + 1)
        press_not_state = rsolve(light, pressed, idx + 1)
        if len(press_state) < len(press_not_state):
            return press_state
        else:
            return press_not_state

    res = rsolve(light, [], 0)
    return res if res != float("inf") else -1


with open("2025_10_input.txt") as f:
    datas = f.readlines()
    total_sum_1 = total_sum_2 = 0
    for data in datas:
        light, *buttons, joltage = data.split()
        light = [int(i == "#") for i in light[1:-1]]
        buttons = [[int(c) for c in b[1:-1].split(",")] for b in buttons]
        joltage = [int(i) for i in joltage[1:-1].split(",")]
        total_sum_1 += len(solve(light, buttons))
    print(total_sum_1)
# a = solve([0, 1, 1, 0], [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]])
# a = solve([0, 1, 1, 0], [[0, 2], [0, 1]])
