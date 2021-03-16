from typing import Iterable


def get_sep_zero_id(array: Iterable) -> int:
    return [int(i) for i in array].index(0)


if __name__ == '__main__':
    print(get_sep_zero_id('111111111111111111111111100000000'))
    print(get_sep_zero_id((1, 0, 0, 0)))
    print(get_sep_zero_id([1, 1, 1, 0]))