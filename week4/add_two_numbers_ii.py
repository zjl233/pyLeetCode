from utils.listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        # 每次将新节点插入 dummy 后面
        # dummy->null
        dummy = ListNode(-1)
        carry = 0
        while s1 or s2 or carry != 0:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            sum_ = a + b + carry
            carry = sum_ // 10
            val = sum_ % 10
            node = ListNode(val)
            node.next = dummy.next
            dummy.next = node

        return dummy.next
