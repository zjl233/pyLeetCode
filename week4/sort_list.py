from utils.listnode import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 洗数据
        if not head or not head.next:
            return head

        res = self.process(head)
        return res

    def get_left_mid(self, head) -> ListNode:
        # 不接受空节点和单节点
        if not head or not head.next:
            raise ValueError('list must have at least two element')

        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 洗数据
        if not l1 or not l2:
            return l1 or l2

        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 or l2

        return dummy.next

    def process(self, head: ListNode):
        # base case
        if not head or not head.next:
            return head

        # 拿到中间的左节点，方便断开连接
        left_mid = self.get_left_mid(head)
        mid = left_mid.next
        left_mid.next = None

        # 排序左半边和右半边
        lh = self.process(head)
        rh = self.process(mid)
        res = self.mergeTwoLists(lh, rh)
        return res
