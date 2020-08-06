from week6.graph import Node


def dfs(node: Node) -> None:
    if not node:
        return

    visited = {node}
    stack = [node]
    print(node.val)

    while stack:
        cur = stack.pop()
        for n in cur.nexts:
            if n not in visited:
                # cur 还有可能还有没遍历完的邻居，还要放会栈里
                stack.append(cur)
                visited.add(n)
                stack.append(n)
                # 第一次以邻居的身份被遍历到时，打印
                print(n.val)
                break
