from utils.listnode import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 洗数据
        if not head:
            return head

        # 哑节点，方便删除头节点的情况
        # 最后结果返回 dummy.next
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                prev.next = prev.next.next
                break
            prev, cur = prev.next, cur.next

        return dummy.next
