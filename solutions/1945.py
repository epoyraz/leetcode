from collections import defaultdict

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        user_minutes = defaultdict(set)
        for user_id, t in logs:
            user_minutes[user_id].add(t)
        answer = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            if 1 <= uam <= k:
                answer[uam - 1] += 1
        return answer
