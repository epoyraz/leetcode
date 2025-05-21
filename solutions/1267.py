class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        seen = {}

        # First pass: store the last occurrence of each prefix sum
        node = dummy
        while node:
            prefix_sum += node.val
            seen[prefix_sum] = node
            node = node.next

        # Second pass: skip nodes between same prefix sums
        prefix_sum = 0
        node = dummy
        while node:
            prefix_sum += node.val
            node.next = seen[prefix_sum].next
            node = node.next

        return dummy.next