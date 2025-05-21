# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseEvenLengthGroups(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr = head
        group_size = 1
        
        while curr:
            # 1) Count how many nodes are in this group (up to group_size)
            count = 0
            node = curr
            while node and count < group_size:
                node = node.next
                count += 1
            next_group_head = node
            
            # 2) If even length, reverse; else leave as is
            if count % 2 == 0:
                # Reverse 'count' nodes starting at curr
                prev = next_group_head
                node_to_rev = curr
                for _ in range(count):
                    nxt = node_to_rev.next
                    node_to_rev.next = prev
                    prev = node_to_rev
                    node_to_rev = nxt
                # Link into list
                prev_group_tail.next = prev
                new_tail = curr  # curr is now tail of reversed group
            else:
                # No reversal: the group stays [curr ... new_tail]
                new_tail = curr
                for _ in range(count - 1):
                    new_tail = new_tail.next
            
            # 3) Advance pointers for next iteration
            prev_group_tail = new_tail
            curr = next_group_head
            group_size += 1
        
        return dummy.next
