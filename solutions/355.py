import collections
import heapq

class Twitter(object):
    def __init__(self):
        self.time = 0
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        heap = []
        users = self.following[userId] | {userId}
        for user in users:
            heap.extend(self.tweets[user])
        heapq.heapify(heap)
        res = []
        for _ in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
