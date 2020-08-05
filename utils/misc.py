from typing import List, Dict
from typing import TypeVar, Generic

T = TypeVar('T')


class UnionFind(Generic[T]):
    # 为了让 int 可以使用引用，而包了一层
    def __init__(self, datas: List[T] = None) -> None:
        if datas is None:
            datas = []

        # 父亲节点。一开始 每个节点的父亲节点都是自己。把父亲节点为自己的节点称为头节点
        # father 向上一次
        # head 一直向上
        self.father: Dict[T, T] = {}
        # 每个头节点所在的集合，一共有多少元素。同时这个 size dict 的大小也是可以得出头节点的个数
        self.size: Dict[T, int] = {}

        # 为什么这样命名 map，father[node1]，node1 的 father 简单易懂

        for data in datas:
            self.father[data] = data
            self.size[data] = 1

    def is_same_set(self, a: T, b: T) -> bool:
        if (a not in self.father) or (b not in self.father):
            return False
        return self.find_head(a) == self.find_head(b)

    # 将较小 set 的头节点，指向较大 set 的头节点
    def union(self, a: T, b: T) -> None:
        if (a not in self.father) or (b not in self.father):
            return

        ha, hb = self.find_head(a), self.find_head(b)
        if ha == hb:
            return

        # 始终确保 head a > head b
        # print(ha, hb)
        if self.size[ha] < self.size[hb]:
            ha, hb = hb, ha
        # 将小的集合连接到大集合上
        self.father[hb] = ha
        self.size[ha] += self.size[hb]
        del self.size[hb]

    # 带路径压缩的
    def find_head(self, na: T) -> T:
        head = na
        path: List[T] = []
        # head 节点是 father 指向自身的节点
        # 如果 father 不指向自身，就一直向上找
        while head != self.father[head]:
            path.append(head)
            head = self.father[head]

        # 将沿途的 node 的 father 都设置为 head
        for node in path:
            self.father[node] = head
        return head

    # 追加新 node
    def add_node(self, data: T) -> None:
        if data in self.father:
            return
            # raise ValueError("duplicate node error")

        self.father[data] = data
        self.size[data] = 1

    # 一共有多少个 set
    def set_num(self) -> int:
        return len(self.size)
