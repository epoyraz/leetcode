# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        return prev

    def reverseListRecursive(self, head):
        if not head or not head.next:
            return head
        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p
