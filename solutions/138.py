class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Map from original node -> cloned node
        old_to_new = {}

        # First pass: clone all nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: assign next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]
