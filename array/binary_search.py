from typing import Callable


def partition_point(
        p0: int, p1: int,
        predicate: Callable[[int], bool]
) -> int:
    if p0 >= p1:
        return p0

    p_bound = p0 + (p1 - p0) // 2
    if predicate(p_bound):
        return partition_point(p_bound + 1, p1, predicate)

    return partition_point(p0, p_bound, predicate)
