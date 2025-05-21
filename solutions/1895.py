class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        answer = [0] * n
        
        # Left to right pass
        moves = 0
        balls = 0
        for i in range(n):
            answer[i] += moves
            balls += int(boxes[i])
            moves += balls
        
        # Right to left pass
        moves = 0
        balls = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            balls += int(boxes[i])
            moves += balls
        
        return answer
