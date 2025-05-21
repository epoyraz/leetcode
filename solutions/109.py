# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None

        def find_mid(left, right):
            slow = fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def build(left, right):
            if left == right:
                return None
            mid = find_mid(left, right)
            root = TreeNode(mid.val)
            root.left = build(left, mid)
            root.right = build(mid.next, right)
            return root

        return build(head, None)
