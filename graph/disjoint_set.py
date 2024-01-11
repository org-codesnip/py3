class DisjointSet:
    def __init__(self, n: int):
        self.parents = list(range(n))

    def query(self, token: int) -> int:
        assert token < len(self.parents)

        token_next = self.parents[token]
        if token_next == token:
            return token

        # Path compression
        token_next = self.query(token_next)
        self.parents[token] = token_next

        return token_next

    def link(self, token_0: int, token_1: int):
        token_0 = self.query(token_0)
        token_1 = self.query(token_1)
        if token_0 == token_1:
            return

        self.parents[token_1] = token_0
