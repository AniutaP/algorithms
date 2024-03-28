from typing import TypeVar, Generic


__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self, visited=None) -> list[Node]:
        if visited is None:
            visited = []
        visited.append(self._root)
        if not self._root.outbound:
            return visited
        for node in self._root.outbound:
            if node not in visited:
                g = Graph(node)
                g.dfs(visited)

        return visited

    def bfs(self) -> list[Node]:
        if not self._root.outbound:
            return [self._root]
        queue = [self._root]
        visited = [self._root]
        while queue:
            if queue[0].outbound:
                for node in queue[0].outbound:
                    if node not in queue and node not in visited:
                        queue.append(node)
                        visited.append(node)
            queue.pop(0)

        return visited
