from collections import deque

from week6.graph import Node


def bfs(node: Node) -> None:
    if not node:
        return

    queue = deque([node])
    visited = {node}

    while queue:
        cur = queue.popleft()
        print(cur.val)
        for n in cur.nexts:
            if n not in visited:
                queue.append(n)
                visited.add(n)
