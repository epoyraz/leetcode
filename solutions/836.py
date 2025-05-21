import collections

class Solution(object):
    def racecar(self, target):
        queue = collections.deque([(0, 1, 0)])  # (position, speed, steps)
        visited = set((0, 1))
        
        while queue:
            pos, speed, steps = queue.popleft()
            if pos == target:
                return steps
            
            # Accelerate
            next_pos, next_speed = pos + speed, speed * 2
            if (next_pos, next_speed) not in visited and 0 <= next_pos <= 2 * target:
                visited.add((next_pos, next_speed))
                queue.append((next_pos, next_speed, steps + 1))
            
            # Reverse
            next_speed = -1 if speed > 0 else 1
            if (pos, next_speed) not in visited:
                visited.add((pos, next_speed))
                queue.append((pos, next_speed, steps + 1))
