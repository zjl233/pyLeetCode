from typing import List, Optional, Deque

from utils.treenode import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        vals = self.tree_to_vals(root)
        vals_str = str(vals).replace("None", "null")

        return vals_str

    def tree_to_vals(self, root: TreeNode) -> List[Optional[int]]:
        if not root:
            return [None]

        vals = [root.val]
        vals.extend(self.tree_to_vals(root.left))
        vals.extend(self.tree_to_vals(root.right))

        return vals

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals_str = data.replace("null", "None")
        vals = eval(vals_str)

        root = self.vals_to_tree(vals)

        return root

    def vals_to_tree(self, vals: List[Optional[int]]) -> Optional[TreeNode]:
        if not vals:
            return None

        val = vals.pop(0)
        if val is None:
            return None

        root = TreeNode(val)
        root.left = self.vals_to_tree(vals)
        root.right = self.vals_to_tree(vals)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
