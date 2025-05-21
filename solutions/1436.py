from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        n = len(friends)
        seen = set([id])
        queue = deque([id])
        for _ in range(level):
            for _ in range(len(queue)):
                curr = queue.popleft()
                for f in friends[curr]:
                    if f not in seen:
                        seen.add(f)
                        queue.append(f)

        freq = Counter()
        for friend in queue:
            freq.update(watchedVideos[friend])
        
        return sorted(freq.keys(), key=lambda x: (freq[x], x))
