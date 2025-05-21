class Solution:
    def minimumRounds(self, tasks):
        from collections import Counter
        cnt = Counter(tasks)
        rounds = 0
        for f in cnt.values():
            if f == 1:
                return -1
            # minimum number of batches of size 2 or 3 to cover f tasks
            rounds += (f + 2) // 3
        return rounds
