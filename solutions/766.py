"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):
        if not head:
            return head
        
        def flatten_dfs(prev, curr):
            if not curr:
                return prev
            curr.prev = prev
            prev.next = curr
            
            # Save next because current.next may be overwritten after child flatten
            temp_next = curr.next
            
            tail = flatten_dfs(curr, curr.child)
            curr.child = None  # clear child after flattening
            
            return flatten_dfs(tail, temp_next)
        
        dummy = Node(0)
        flatten_dfs(dummy, head)
        
        dummy.next.prev = None
        return dummy.next