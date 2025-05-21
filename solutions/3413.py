from collections import deque

class Solution(object):
    def findWinningPlayer(self, skills, k):
        """
        :type skills: List[int]
        :type k: int
        :rtype: int
        """
        n = len(skills)
        # If k >= n, the best player (max skill) will inevitably win n-1 in a row
        # before anyone else can, so we can return its index immediately.
        if k >= n:
            # Unique skills â index of max
            return skills.index(max(skills))
        
        # Initialize the âcurrent championâ and a queue of challengers.
        # We store (skill, index) tuples.
        champ_skill = skills[0]
        champ_idx   = 0
        wins = 0
        
        dq = deque()
        for i in range(1, n):
            dq.append((skills[i], i))
        
        # Simulate until someone reaches k consecutive wins
        while True:
            opp_skill, opp_idx = dq.popleft()
            
            if champ_skill > opp_skill:
                # champion wins
                wins += 1
                # loser goes to back
                dq.append((opp_skill, opp_idx))
            else:
                # challenger becomes new champion
                dq.append((champ_skill, champ_idx))
                champ_skill, champ_idx = opp_skill, opp_idx
                wins = 1
            
            if wins == k:
                return champ_idx
