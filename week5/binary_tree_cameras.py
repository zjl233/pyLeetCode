from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    # 成为待侦测节点，所需的最少 摄像头
    undetected: int = 0
    detected: int = 0
    # 未什么要设为 inf，考虑只有两个节点的情况
    camera: int = float('inf')


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0

        info = self.process(root)
        return min(info.detected, info.camera)

    def process(self, root) -> Info:
        if not root:
            return Info()

        l = self.process(root.left)
        r = self.process(root.right)

        undetected = l.detected + r.detected
        detected = min(
            l.camera + r.camera,
            l.camera + r.detected,
            r.camera + l.detected,
        )
        camera = 1 + min(l) + min(r)
        return Info(undetected, detected, camera)
