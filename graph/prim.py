from typing import List, Tuple

import heapq


def prim(
        graph: List[List[Tuple[int, int]]]
) -> List[Tuple[Tuple[int, int], int]]:
    ret = []

    visited = [False for _ in range(len(graph))]
    heap = [(0, (0, 0))]
    while heap:
        weight, (v, v_prev) = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True

        for (v_next, weight_next) in graph[v]:
            heapq.heappush(heap, (weight_next, (v_next, v)))

        ret.append(((v_prev, v), weight))

    ret.reverse()
    ret.pop()

    return ret
