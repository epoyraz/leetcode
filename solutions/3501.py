class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        remove = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        
        while curr:
            if curr.val in remove:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
