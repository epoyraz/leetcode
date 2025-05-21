# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Count the total number of nodes
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # Determine the size of each part
        base_size, remainder = divmod(n, k)
        # The first 'remainder' parts get an extra node
        
        parts = []
        curr = head
        for i in range(k):
            part_head = curr
            # Determine the correct size for this part
            size = base_size + (1 if i < remainder else 0)
            # Advance to the end of this part
            for j in range(size - 1):
                if curr:
                    curr = curr.next
            # Cut the list if needed
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            # Append head of this part (or None)
            parts.append(part_head)
        
        return parts
