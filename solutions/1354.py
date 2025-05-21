class Solution(object):
    def findWinners(self, matches):
        loss = {}
        players = set()
        for w, l in matches:
            players.add(w)
            players.add(l)
            loss[l] = loss.get(l, 0) + 1
        no_loss = []
        one_loss = []
        for p in sorted(players):
            cnt = loss.get(p, 0)
            if cnt == 0:
                no_loss.append(p)
            elif cnt == 1:
                one_loss.append(p)
        return [no_loss, one_loss]
