from typing import List, Tuple, Optional

import heapq


def dijkstra(
        graph: List[List[Tuple[int, int]]],
        src: int,
) -> List[Optional[int]]:
    ret: List[Optional[int]] = [None for _ in range(len(graph))]

    heap = [(0, src)]
    while heap:
        dist, v = heapq.heappop(heap)
        if ret[v] is not None and ret[v] <= dist:
            continue
        ret[v] = dist

        for (v_next, w) in graph[v]:
            heapq.heappush(heap, (dist + w, v_next))

    return ret
