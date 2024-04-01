from typing import TypeVar, Generic
import queue


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

    def dfs(self) -> list[Node]:
        visited = []

        def inner(node):
            visited.append(node)
            if not node.outbound:
                return visited
            for bound_node in node.outbound:
                if bound_node not in visited:
                    inner(bound_node)

        inner(self._root)

        return visited

    def bfs(self) -> list[Node]:
        nodes_queue = queue.Queue()
        nodes_queue.put(self._root)
        visited = [self._root]
        while not nodes_queue.empty():
            current_node = nodes_queue.get()
            if current_node.outbound:
                for node in current_node.outbound:
                    if node not in visited:
                        nodes_queue.put(node)
                        visited.append(node)

        return visited
