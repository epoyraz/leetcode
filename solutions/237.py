# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: None
        """
        node.val = node.next.val
        node.next = node.next.next
