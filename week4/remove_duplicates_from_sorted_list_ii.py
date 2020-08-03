from utils.listnode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 洗数据
        if not head or not head.next:
            return head

        # 可能有头节点变动的情况，要哑节点
        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy
        while cur and cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                end = cur.next.next
                while end and end.val == cur.next.val:
                    end = end.next
                cur.next = end
            else:
                cur = cur.next

        return dummy.next
