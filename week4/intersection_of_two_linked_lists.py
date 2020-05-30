from typing import Optional

from utils.listnode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        # 常见错误，将 headA 和 headB 作为遍历节点
        curA, curB = headA, headB
        # 相交：指向统一节点
        # 不相交：指向不同的 None，但是 None is None
        while curA is not curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA
