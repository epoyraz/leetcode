# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteMiddle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If there's only one node, removing it leaves an empty list.
        if not head.next:
            return None
        
        prev = None
        slow = head
        fast = head
        
        # Move fast by 2 and slow by 1. When fast reaches end, slow is at middle.
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Remove the middle node (slow) by linking previous around it.
        prev.next = slow.next
        
        return head
