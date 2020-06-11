from typing import NamedTuple


class Info(NamedTuple):
    in_: int = 0
    out: int = 0


if __name__ == '__main__':
    i1 = Info(1, 1)
    i2 = Info(1, 2)
    print(i1 + i2)