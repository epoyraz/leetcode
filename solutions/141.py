# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next         # Move slow pointer by 1
            fast = fast.next.next    # Move fast pointer by 2
            if slow == fast:
                return True

        return False
