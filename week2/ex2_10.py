if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        _ = int(line)
        strs = sys.stdin.readline().split()
        nums = [int(s) for s in strs]
        desc = int(sys.stdin.readline()) == 1
        nums.sort(reverse=desc)
        print(' '.join(map(str, nums)))
