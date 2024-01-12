from typing import List, Callable


class SegmentTree:
    def __init__(self, vec: List[int], op: Callable[[int, int], int]):
        self.n: int = len(vec)
        self.op = op

        inner: List[int] = [0 for _ in vec] + vec
        for i in reversed(range(1, self.n)):
            inner[i] = op(inner[i * 2], inner[i * 2 + 1])
        self.inner = inner

    def query(self, p0: int, p1: int) -> int:
        if p0 >= p1:
            return 0
        assert p1 <= self.n

        p0 = p0 + self.n
        p1 = p1 + self.n - 1

        self.__query_impl(p0, p1)

    def __query_impl(self, p0: int, p1: int) -> int:
        ret = 0
        if p0 > p1:
            return ret

        if p0 % 2 > 0:
            ret = self.op(ret, self.inner[p0])
        if p1 % 2 < 1:
            ret = self.op(ret, self.inner[p1])

        p0_next, p1_next = ((p0 + 1) // 2, (p1 - 1) // 2)
        ret = self.op(ret, self.__query_impl(p0_next, p1_next))

        return ret

    def update(self, index: int, val_next: int):
        assert index < self.n

        p0 = index + self.n
        self.inner[p0] = val_next

        self.__update_impl(p0 // 2)

    def __update_impl(self, p0: int):
        if p0 < 1:
            return

        child_0, child_1 = (p0 * 2, p0 * 2 + 1)
        self.inner[p0] = self.op(self.inner[child_0], self.inner[child_1])

        self.__update_impl(p0 // 2)
