from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n
        self.setCount = n  # 当前连通分量数目

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False

        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def check(self, a: str, b: str) -> bool:
        cnt = 0
        for ac, bc in zip(a, b):
            if ac != bc:
                cnt += 1
                if cnt > 2:
                    return False
        return True

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if uf.connected(i, j):
                    continue
                if self.check(strs[i], strs[j]):
                    uf.unite(i, j)
        return uf.setCount
