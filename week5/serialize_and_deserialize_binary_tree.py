from collections import deque
from typing import List, Optional, Deque

from utils.treenode import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        def process(node: TreeNode) -> List[Optional[int]]:
            if not node:
                return [None]

            vals = [node.val]
            vals.extend(process(node.left))
            vals.extend(process(node.right))

            return vals

        res = str(process(root))
        # 题意，将 None 全部替换成 null
        res.replace("None", "null")
        return res

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        s = data.replace("null", "None")
        vals: Deque[Optional[int]] = deque(eval(s))

        def process(ints: Deque[Optional[int]]) -> Optional[TreeNode]:
            if not ints:
                return None

            val = ints.popleft()
            if val is None:
                return None

            root = TreeNode(int(val))
            root.left = process(ints)
            root.right = process(ints)

            return root

        res = process(vals)

        return res

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
