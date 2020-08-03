import sys
from copy import deepcopy
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'TreeNode({self.val!r})'

    def serialize(self, root: 'TreeNode') -> str:
        if not root:
            return ""

        vals = self.tree_to_vals(root)
        vals_str = str(vals).replace("None", "null")

        return vals_str

    def tree_to_vals(self, root: 'TreeNode') -> List[Optional[int]]:
        if not root:
            return [None]

        vals = [root.val]
        vals.extend(self.tree_to_vals(root.left))
        vals.extend(self.tree_to_vals(root.right))

        return vals

    def deserialize(self, data: str) -> Optional['TreeNode']:
        if not data:
            return None

        vals_str = data.replace("null", "None")
        vals = eval(vals_str)

        root = self.vals_to_tree(vals)

        return root

    def vals_to_tree(self, vals: List[Optional[int]]) -> Optional['TreeNode']:
        if not vals:
            return None

        val = vals.pop(0)
        if val is None:
            return None

        root = TreeNode(val)
        root.left = self.vals_to_tree(vals)
        root.right = self.vals_to_tree(vals)

        return root

    # from copy import deepcopy as deepcopy
    # import sys
    #
    #
    # class TreeNode:
    #     def __init__(self, val=None):
    #         self.val = val
    #         self.left = None
    #         self.right = None
    # https://github.com/jdmcpeek/pretty-print-binary-tree
    def visit(self):
        sys.stdout.write(self.val)

    def getNumNodes(self):
        total = 0
        if self.left:
            total += self.left.getNumNodes()
        if self.right:
            total += self.right.getNumNodes()
        return total + 1

    @classmethod
    def createTree(cls, depth):
        tree = TreeNode('X')
        cls.createTreeHelper(tree, depth, 1)
        return tree

    @classmethod
    def createTreeHelper(cls, node, depth, cur):
        if cur == depth:
            return
        node.left = TreeNode('X')
        node.right = TreeNode('XX')
        cls.createTreeHelper(node.left, depth, cur + 1)
        cls.createTreeHelper(node.right, depth, cur + 1)

    def getHeight(self):
        return TreeNode.getHeightHelper(self)

    @staticmethod
    def getHeightHelper(node):
        if not node:
            return 0
        else:
            return max(TreeNode.getHeightHelper(node.left), TreeNode.getHeightHelper(node.right)) + 1

    def fillTree(self, height):
        TreeNode.fillTreeHelper(self, height)

    def fillTreeHelper(node, height):
        if height <= 1:
            return
        if node:
            if not node.left: node.left = TreeNode(' ')
            if not node.right: node.right = TreeNode(' ')
            TreeNode.fillTreeHelper(node.left, height - 1)
            TreeNode.fillTreeHelper(node.right, height - 1)

    def entire_tree(self) -> str:
        """
        """
        # final result
        s = ''

        # get height of tree
        total_layers = self.getHeight()

        tree = deepcopy(self)

        tree.fillTree(total_layers)
        # start a queue for BFS
        queue = Queue()
        # add root to queue
        queue.enqueue(tree)  # self = root
        # index for 'generation' or 'layer' of tree
        gen = 1
        # BFS main
        while not queue.isEmpty():
            # copy queue
            #
            copy = Queue()
            while not queue.isEmpty():
                copy.enqueue(queue.dequeue())
            #
            # end copy queue

            first_item_in_layer = True
            edges_string = ""
            extra_spaces_next_node = False

            # modified BFS, layer by layer (gen by gen)
            while not copy.isEmpty():

                node = copy.dequeue()

                # -----------------------------
                # init spacing
                spaces_front = pow(2, total_layers - gen + 1) - 2
                spaces_mid = pow(2, total_layers - gen + 2) - 2
                dash_count = pow(2, total_layers - gen) - 2
                if dash_count < 0:
                    dash_count = 0
                spaces_mid = spaces_mid - (dash_count * 2)
                spaces_front = spaces_front - dash_count
                init_padding = 2
                spaces_front += init_padding
                if first_item_in_layer:
                    edges_string += " " * init_padding
                # ----------------------------->

                # -----------------------------
                # construct edges layer
                edge_sym = "/" if node.left and node.left.val != " " else " "
                if first_item_in_layer:
                    edges_string += " " * (pow(2, total_layers - gen) - 1) + edge_sym
                else:
                    edges_string += " " * (pow(2, total_layers - gen + 1) + 1) + edge_sym
                edge_sym = "\\" if node.right and node.right.val != " " else " "
                edges_string += " " * (pow(2, total_layers - gen + 1) - 3) + edge_sym
                # ----------------------------->

                # -----------------------------
                # conditions for dashes
                if node.left and node.left.val == " ":
                    dash_left = " "
                else:
                    dash_left = "_"

                if node.right and node.right.val == " ":
                    dash_right = " "
                else:
                    dash_right = "_"
                # ----------------------------->

                # -----------------------------
                # handle condition for extra spaces when node lengths don't match or are even:
                if extra_spaces_next_node:
                    extra_spaces = 1
                    extra_spaces_next_node = False
                else:
                    extra_spaces = 0
                # ----------------------------->

                # -----------------------------
                # account for longer val
                val_length = len(str(node.val))
                if val_length > 1:
                    if val_length % 2 == 1:  # odd
                        if dash_count > 0:
                            dash_count -= ((val_length - 1) / 2)
                        else:
                            spaces_mid -= (val_length - 1) / 2
                            spaces_front -= (val_length - 1) / 2
                            if val_length != 1:
                                extra_spaces_next_node = True
                    else:  # even
                        if dash_count > 0:
                            dash_count -= ((val_length) / 2) - 1
                            extra_spaces_next_node = True
                            # dash_count += 1
                        else:
                            spaces_mid -= (val_length - 1)
                            spaces_front -= (val_length - 1)
                # ----------------------------->

                # -----------------------------
                # print node with/without dashes
                if first_item_in_layer:
                    s += (" " * spaces_front) + (dash_left * dash_count) + str(node.val) + (dash_right * dash_count) + ' '
                    print((" " * spaces_front) + (dash_left * dash_count) + str(node.val) + (dash_right * dash_count), end=' ')
                    first_item_in_layer = False
                else:
                    s += (" " * (spaces_mid - extra_spaces)) + (dash_left * dash_count) + str(node.val) + (dash_right * dash_count) + ' '
                    print((" " * (spaces_mid - extra_spaces)) + (dash_left * dash_count) + str(node.val) + (dash_right * dash_count), end=' ')
                # ----------------------------->

                if node.left: queue.enqueue(node.left)
                if node.right: queue.enqueue(node.right)

            # print the fun squiggly lines
            if not queue.isEmpty():
                s += "\n" + edges_string
                print("\n" + edges_string)

            # increase layer index
            gen += 1

        return s


class Queue(object):
    def __init__(self, items=None):
        if items is None:
            self.a = []
        else:
            self.a = items

    def enqueue(self, b):
        self.a.insert(0, b)

    def dequeue(self):
        return self.a.pop()

    def isEmpty(self):
        return self.a == []

    def size(self):
        return len(self.a)


if __name__ == '__main__':
    # prep the tree...
    #
    # layer 1
    root = TreeNode('A')

    # layer 2
    root.left = TreeNode('B')
    root.right = TreeNode('C')

    # layer 3
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')

    root.left.right.right = TreeNode.createTree(2)

    root.right.left = TreeNode('F')
    root.right.right = TreeNode('G')

    # layer 3
    root.left.left.left = TreeNode('H')
    root.left.left.right = TreeNode('I')
    root.left.right.left = TreeNode('J')
    # root.left.right.right = Node('K')
    # root.right.left.left = Node('L')
    # root.right.left.right = Node('M')
    root.right.right.left = TreeNode('N')
    root.right.right.right = TreeNode('O')

    root.entire_tree()


def test_tree() -> TreeNode:
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    return node1
