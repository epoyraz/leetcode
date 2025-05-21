class Solution(object):
    def doubleIt(self, head):
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        head = reverse(head)
        curr = head
        carry = 0

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while curr:
            total = curr.val * 2 + carry
            curr.val = total % 10
            carry = total // 10
            prev = curr
            curr = curr.next

        if carry:
            prev.next = ListNode(carry)

        return reverse(head)
