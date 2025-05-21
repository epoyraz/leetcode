class Solution:
    def mergeNodes(self, head):
        dummy = ListNode(0)
        tail = dummy
        curr = head.next
        summ = 0

        while curr:
            if curr.val == 0:
                tail.next = ListNode(summ)
                tail = tail.next
                summ = 0
            else:
                summ += curr.val
            curr = curr.next

        return dummy.next