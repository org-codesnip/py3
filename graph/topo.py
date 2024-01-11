from typing import List


def topo_sort_kahn(
        graph: List[List[int]]
) -> List[List[int]]:
    indeg_vec = [0 for _ in range(len(graph))]
    for v_vec in graph:
        for v_next in v_vec:
            indeg_vec[v_next] += 1

    ret = []

    breadth = [v for v, indeg in enumerate(indeg_vec) if indeg <= 0]
    while breadth:
        ret.append(breadth)

        breadth_next = []
        for v in breadth:
            for v_next in graph[v]:
                indeg_vec[v_next] -= 1
                if indeg_vec[v_next] > 0:
                    continue
                breadth_next.append(v_next)
        breadth = breadth_next

    return ret
