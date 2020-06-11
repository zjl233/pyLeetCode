from collections import deque
from typing import List, Optional, Deque

from utils.treenode import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        res: List[str] = []
        level = [root]
        while level:
            res.extend([str(n.val) if n else "#" for n in level])

            level = [kid for n in level if n for kid in (n.left, n.right)]

        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        strs = deque(data.split(","))
        root = TreeNode(int(strs.popleft()))
        nodes = deque([root])

        while nodes:
            cur = nodes.popleft()
            left_val = strs.popleft()
            right_val = strs.popleft()

            left = TreeNode(int(left_val)) if left_val != "#" else None
            right = TreeNode(int(right_val)) if right_val != "#" else None

            cur.left = left
            cur.right = right

            nodes.append(left) if left else None
            nodes.append(right) if right else None

        return root

    def serialize_recursive(self, root: TreeNode) -> str:
        if not root:
            return ""

        def process(cur: TreeNode, data: List[str]):
            if not cur:
                data.append("#")
                return

            data.append(str(cur.val))
            process(cur.left, data)
            process(cur.right, data)

        res: List[str] = []
        process(root, res)
        return ",".join(res)

    def deserialize_recursive(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        def process(vals: Deque[str]):
            if not vals:
                return None

            val = vals.popleft()
            if val == "#":
                return None

            root = TreeNode(int(val))  # dq

            root.left = process(vals)
            root.right = process(vals)

            return root

        strs = deque(data.split(","))
        r = process(strs)

        return r

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        str1 = self.serialize_recursive(s)
        str2 = self.serialize_recursive(t)
        return str2 in str1

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
