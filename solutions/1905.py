class AuthenticationManager(object):

    def __init__(self, timeToLive):
        self.timeToLive = timeToLive
        self.tokens = {}  # tokenId -> expiryTime

    def generate(self, tokenId, currentTime):
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId, currentTime):
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime):
        return sum(1 for expiry in self.tokens.values() if expiry > currentTime)
