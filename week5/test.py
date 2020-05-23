# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 无法解决节点重合的问题
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        info = self.process(root, p, q)
        return info[1]

    def process(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not TreeNode:
            return [0, None]

        linfo = self.process(root.left, p, q)
        rinfo = self.process(root.right, p, q)

        # 每次，先计算子树中 p q 的个数
        count = 0
        if root == p:
            count += 1
        if root == q:
            count += 1

        count += linfo[0]
        count += rinfo[0]

        if count == 2 and not linfo[1] and not rinfo[1]:
            return [count, root]
        elif linfo[1]:
            return [count, linfo[1]]
        elif rinfo[1]:
            return [count, rinfo[1]]
        else:
            return [count, None]

        # return count, ancestor: TreeNode


if __name__ == '__main__':
    def mutable(nums):
        print(id(nums))  # 1437494204232
        nums += [4]
        print(id(nums))  # 1437494204232


    def immutable(num):
        print(id(num))  # 2006430784
        num += 1
        print(id(num))  # 2006430816


    a = [1, 2, 3]
    print(id(a))  # 1437494204232

    mutable(a)

    b = 1
    print(id(b))  # 2006430784

    immutable(b)

    d = {(1, 2): 'x'}
    print(d[(1, 2)])
