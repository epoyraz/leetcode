
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        def compute_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        curr = head
        while curr and curr.next:
            g = compute_gcd(curr.val, curr.next.val)
            new_node = ListNode(g, curr.next)
            curr.next = new_node
            curr = new_node.next
        return head
