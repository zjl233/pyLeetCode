from utils.treenode import TreeNode


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        found = False

        def process(node):
            nonlocal successor
            nonlocal found
            nonlocal p

            if not node:
                return

            process(node.left)

            if found:
                successor = node
                found = False
                return

            if node is p:
                found = True

            process(node.right)

            return

        process(root)

        return successor
