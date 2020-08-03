from typing import NamedTuple, Tuple, List


# robot: (time, level)
# task: (time. level)
class Pair(NamedTuple):
    time: int
    level: int


def assign_task(robots: List[Tuple[int, int]], tasks: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    题目地址：
    https://www.nowcoder.com/study/live/350/2/6
    课后作业3-安排机器
    pypy 3.6.1

    题型：
    贪心

    解题思路：
    每次统计”刚好“在时间上满足要求的机器人
    再从刚好满足时间要求的机器人里，挑一个等级最低的

    参考：
    https://www.nowcoder.com/questionTerminal/42e7ff5c5696445ab907caff17fc9e15
    @xiao_coco

    难度评价：
    <<思维[想不到] Coding[有点绕]>>

    time: O(n)
    space: O(n)
    ac: 100%
    注：用 NamedTuple 会超内存

    """
    # robots = [Pair(t, l) for t, l in robots_]
    # tasks = [Pair(t, l) for t, l in tasks_]

    robots.sort(reverse=True)
    tasks.sort(reverse=True)
    # robots.sort(key=lambda robot: 200 * robot.time + 3 * robot.level)
    # tasks.sort(key=lambda task: 200 * task.time + 3 * task.level, reverse=True)

    cnt = 0  # 完成的任务数
    profit = 0  # 利润

    # 统计每个 level 有几台 robot
    levels = [0 for _ in range(101)]
    # 指向 robots 的指针，表明已经统计了多少台 robot
    j = 0
    for task in tasks:
        # 统计，在时间上，可以完成当前 task 的 robot
        while j < len(robots):
            robot = robots[j]
            if robot[0] >= task[0]:
                levels[robot[1]] += 1
                j += 1
            else:
                # 碰到了 robot[0] < task[0] 的情况，应为数组是按照 time 排的，所有后面的 robot 时间也都小于 task 时间
                break

        # 分配 task 给 robot，找在等级上，刚好可以满足要求（也就是略大于 task）的 robot
        # levels 数组的长度为 101, 100 是等级上限，
        for i in range(task[1], len(levels)):
            # 有满足条件的机器人
            # 注：上一个 while 保证 time，这个 for 保证 level
            if levels[i] != 0:
                cnt += 1
                profit += 200 * task[0] + 3 * task[1]
                levels[i] -= 1
                break

    return cnt, profit

# 用 NamedTuple 会超内存
# def assign_task(robots_: List[Tuple[int, int]], tasks_: List[Tuple[int, int]]) -> Tuple[int, int]:
#     """
#     题目地址：
#     https://www.nowcoder.com/study/live/350/2/6
#     课后作业3-安排机器
#     pypy 3.6.1
#
#     题型：
#     贪心
#
#     解题思路：
#     每次统计”刚好“在时间上满足要求的机器人
#     再从刚好满足时间要求的机器人里，挑一个等级最低的
#
#     参考：
#     https://www.nowcoder.com/questionTerminal/42e7ff5c5696445ab907caff17fc9e15
#     @xiao_coco
#
#     难度评价：
#     <<思维[想不到] Coding[有点绕]>>
#
#     time: O(n log n, n^2, 2^n)
#     space: O(n log n, n^2, 2^n)
#     ac: 100%
#     """
#     robots = [Pair(t, l) for t, l in robots_]
#     tasks = [Pair(t, l) for t, l in tasks_]
#
#     del robots_
#     del tasks_
#
#     robots.sort(reverse=True)
#     tasks.sort(reverse=True)
#     # robots.sort(key=lambda robot: 200 * robot.time + 3 * robot.level)
#     # tasks.sort(key=lambda task: 200 * task.time + 3 * task.level, reverse=True)
#
#     cnt = 0  # 完成的任务数
#     profit = 0  # 利润
#
#     # 统计每个 level 有几台 robot
#     levels = [0 for _ in range(101)]
#     # 指向 robots 的指针，表明已经统计了多少台 robot
#     j = 0
#     for task in tasks:
#         # 统计，在时间上，可以完成当前 task 的 robot
#         while j < len(robots):
#             robot = robots[j]
#             if robot.time >= task.time:
#                 levels[robot.level] += 1
#                 j += 1
#             else:
#                 # 碰到了 robot.time < task.time 的情况，应为数组是按照 time 排的，所有后面的 robot 时间也都小于 task 时间
#                 break
#
#         # 分配 task 给 robot，找在等级上，刚好可以满足要求（也就是略大于 task）的 robot
#         # levels 数组的长度为 101, 100 是等级上限，
#         for i in range(task.level, len(levels)):
#             # 有满足条件的机器人
#             # 注：上一个 while 保证 time，这个 for 保证 level
#             if levels[i] != 0:
#                 cnt += 1
#                 profit += 200 * task.time + 3 * task.level
#                 levels[i] -= 1
#                 break
#
#     return cnt, profit


def oj_main():
    n, m = [int(s) for s in input().split()]

    # robots and tasks
    rs: List[Tuple[int, int]] = []
    for _ in range(n):
        time_str, level_str = input().split()
        rs.append((int(time_str), int(level_str)))

    ts: List[Tuple[int, int]] = []
    for _ in range(m):
        time_str, level_str = input().split()
        ts.append((int(time_str), int(level_str)))

    res = assign_task(rs, ts)
    print(res[0], res[1])


if __name__ == '__main__':
    # 多用例输入
    # 单用例也可以用
    while True:
        try:
            oj_main()
        except EOFError:
            break
