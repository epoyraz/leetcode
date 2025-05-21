from collections import deque

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        found = set(initialBoxes)
        queue = deque()
        opened = set()
        available_keys = set()
        total_candies = 0

        # Add initially open boxes to the queue
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        while queue:
            box = queue.popleft()
            if box in opened:
                continue
            opened.add(box)
            total_candies += candies[box]

            # Collect keys and try to open new boxes
            for key in keys[box]:
                if key not in available_keys:
                    available_keys.add(key)
                    if key in found and key not in opened:
                        queue.append(key)

            # Add contained boxes
            for contained in containedBoxes[box]:
                found.add(contained)
                if status[contained] == 1 or contained in available_keys:
                    queue.append(contained)

        return total_candies
