# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # Dummy node for the new sorted list
        curr = head

        while curr:
            prev = dummy
            # Find the position to insert the current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            next_temp = curr.next  # Save next node to process
            # Insert current node between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            curr = next_temp  # Move to the next node to sort

        return dummy.next
