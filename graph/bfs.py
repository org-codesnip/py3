from typing import List, Optional


def bfs(
        graph: List[List[int]],
        src: int,
) -> List[Optional[int]]:
    ret: List[Optional[int]] = [None] * len(graph)

    water_level = 0
    breadth = [src]
    while breadth:
        breadth_next = []
        for v in breadth:
            if (ret[v] is not None) and ret[v] <= water_level:
                continue
            ret[v] = water_level

            breadth_next += graph[v]

        breadth = breadth_next
        water_level += 1

    return ret
