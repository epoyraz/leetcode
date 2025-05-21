# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNodes(self, head):
        # reverse the linked list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev is the head of reversed list
        max_so_far = 0
        dummy = ListNode(0)
        tail = dummy
        curr = prev
        # keep nodes >= max_so_far
        while curr:
            if curr.val >= max_so_far:
                max_so_far = curr.val
                tail.next = curr
                tail = curr
            curr = curr.next
        tail.next = None
        # reverse back
        prev = None
        curr = dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
