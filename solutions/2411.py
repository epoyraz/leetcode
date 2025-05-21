# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # Initialize m x n matrix filled with -1
        matrix = [[-1] * n for _ in range(m)]
        
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        curr = head
        
        while curr and top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for col in range(left, right + 1):
                if not curr:
                    break
                matrix[top][col] = curr.val
                curr = curr.next
            top += 1
            if not curr:
                break
            
            # Traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                if not curr:
                    break
                matrix[row][right] = curr.val
                curr = curr.next
            right -= 1
            if not curr:
                break
            
            # Traverse from right to left along the bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if not curr:
                        break
                    matrix[bottom][col] = curr.val
                    curr = curr.next
                bottom -= 1
            if not curr:
                break
            
            # Traverse from bottom to top along the left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if not curr:
                        break
                    matrix[row][left] = curr.val
                    curr = curr.next
                left += 1
        
        return matrix
