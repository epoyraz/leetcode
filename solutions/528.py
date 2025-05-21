# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1) Find the k-th node from the beginning
        front = head
        for _ in range(k - 1):
            front = front.next
        
        # 2) Use two-pointer technique to find k-th from the end
        back = head
        runner = front
        while runner.next:
            runner = runner.next
            back = back.next
        
        # 3) Swap their values
        front.val, back.val = back.val, front.val
        
        return head
