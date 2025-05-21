class Solution:
    def getCollisionTimes(self, cars):
        n = len(cars)
        res = [-1.0] * n
        stack = []  # stack of (index)

        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            while stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]
                
                if speed <= speed_j:
                    stack.pop()
                else:
                    time = float(pos_j - pos) / (speed - speed_j)
                    # If j collides later than time or never collides
                    if res[j] == -1 or time <= res[j]:
                        res[i] = time
                        break
                    else:
                        stack.pop()
            stack.append(i)
        return res
