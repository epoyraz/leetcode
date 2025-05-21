class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        # 1) Expand each OFFLINE into an OFF (at t) and an ON (at t+60)
        timeline = []
        for typ, t_str, data in events:
            t = int(t_str)
            if typ == "OFFLINE":
                uid = int(data)
                timeline.append((t,    "OFF", uid))
                timeline.append((t+60, "ON",  uid))
            else:  # MESSAGE
                timeline.append((t, "MSG", data))

        # 2) Sort by (timestamp, kind), **with ON < OFF < MSG** at the same time
        weight = {"ON": 0, "OFF": 1, "MSG": 2}
        timeline.sort(key=lambda ev: (ev[0], weight[ev[1]]))

        # 3) Sweep: track whoâs online and count mentions
        online   = [True] * numberOfUsers
        mentions = [0]    * numberOfUsers

        for _, typ, payload in timeline:
            if typ == "ON":
                online[payload] = True
            elif typ == "OFF":
                online[payload] = False
            else:  # "MSG"
                s = payload
                if s == "ALL":
                    # mention everyone
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                elif s == "HERE":
                    # mention only those currently online
                    for u in range(numberOfUsers):
                        if online[u]:
                            mentions[u] += 1
                else:
                    # explicit tokens e.g. "id3 id0 id3"
                    for tok in s.split():
                        u = int(tok[2:])
                        mentions[u] += 1

        return mentions
