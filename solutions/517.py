class Solution:
    def findMinMoves(self, machines):
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        
        target = total // n
        max_moves = 0
        curr_sum = 0
        
        for load in machines:
            curr = load - target
            curr_sum += curr
            max_moves = max(max_moves, abs(curr_sum), curr)
        
        return max_moves
